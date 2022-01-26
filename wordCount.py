import sys, re


inputFile = open(sys.argv[1], 'r')
output = open(sys.argv[2], 'w')
sys.stdout = output

dictionary = {}

for line in inputFile:
  line = line.strip()
  line = line.lower()
  line = line.replace(',', '')
  for i in re.split(' ', line):
    if i not in dictionary:
      dictionary[i] = 1
    else:
      dictionary[i] +=1

dictionary = dict(sorted(dictionary.items(), key = lambda kv: kv[0]))
for key in list(dictionary.keys()):
  print('%s %s'%(key, dictionary[key]))
output.close()