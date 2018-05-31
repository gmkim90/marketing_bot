import sys
sys.path.append("google_translate_API")
from mtranslate import translate
from tqdm import trange
import pdb
import re

'''
aiml_en = open('ALICE+CONVAI_RULESET_ENG.aiml', 'r')
aiml_ko = open('ALICE+CONVAI_RULESET_KOR.aiml', 'w')
'''

aiml_ko = open('ALICE+CONVAI_RULESET_KOR.aiml', 'a')


#aiml_en = open('ALICE+CONVAI_RULESET_ENG_REST.aiml', 'r')
#aiml_en = open('ALICE+CONVAI_RULESET_ENG_REST_REST.aiml', 'r')
aiml_en = open('ALICE+CONVAI_RULESET_ENG_REST_REST_REST.aiml', 'r')


lines = aiml_en.readlines()

# Logic: if line contain either pattern or template, translator process all the text between brackets (<>)

#for line in lines:
for i in trange(0, len(lines)):
    line = lines[i]
    #print(line)
    pattern_s = line.find('<pattern>')
    pattern_e =line.find('</pattern>')
    template_s = line.find('<template>')
    template_e = line.find('</template>')

    if(pattern_s >= 0 or pattern_e >= 0 or template_s >= 0 or template_e >= 0):
        # Ver1
        # b_l = line.find('<')
        # b_r = line.find('>')

        # Ver2
        b_l = [m.start() for m in re.finditer('<', line)]
        b_r = [m.start() for m in re.finditer('>', line)]

        line_w = line[0:b_r[0]+1]
        assert(len(b_l) == len(b_r))
        for i in range(len(b_l)-1):
            diff =  b_l[i+1] - b_r[i]
            #pdb.set_trace()

            if(diff > 1):
                source = line[b_r[i]+1:b_l[i+1]] # eng
                target = translate(source, 'ko')
                print(source + ' --> ' + target)
                line_w += target
            else:
                line_w += line[b_l[i+1]:b_r[i+1]+1]
        line_w += line[b_l[-1]:]
    else:
        line_w = line

    #print(line_w)
    aiml_ko.write(line_w)


aiml_en.close()
aiml_ko.close()

