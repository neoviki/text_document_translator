from googletrans import Translator
import sys

# translate from any language to English ( any:language supported by google translator )
def get_english_translation(text):
    tran = Translator()
    translator = tran.translate(text, dest='en')
    #print(translator.text)
    return translator.text


if len(sys.argv) < 3:
    print("\nusage: "+sys.argv[0]+" <input_file> <output_file>\n")
    exit(1)

print("\n")

f_in  = sys.argv[1]
f_out = sys.argv[2]


fp_in = open(f_in, "r")
fp_out = open(f_out, "w")

lines = fp_in.readlines()

print("Translation Text File [ " +f_in+" ]\n")
for l in lines:
    
    if len(l.strip()) == 0:
        continue

    ltxt = str(l.strip())
    ttxt = get_english_translation(ltxt)

    print("   "+ltxt)
    print("   "+ttxt)
    print("\n")

    fp_out.write(ltxt)
    fp_out.write("\n")
    fp_out.write(ttxt)
    fp_out.write("\n")
    
    fp_out.write("\n")
    fp_out.write("\n")


fp_in.close()
fp_out.close()
print("\n")
print("Translation Successful!\n")
