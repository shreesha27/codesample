infilename="/Users/Shreesha/Desktop/example.txt"

dict = {}

with open(infilename) as f:
    lines=[line.lower() for line in f]
    for i,l in enumerate(lines):
         for word in l.strip().split(" "):
             if word in dict.keys(): dict[word].append(i+1)
             else:
                 dict[word] = [i+1]


with open(infilename+"_index.txt", 'w') as fl:
    for key,value in sorted(dict.items()):
        fl.write('%s %s\n' % (key, value))


