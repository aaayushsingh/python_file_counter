import os

list = []
counter = []
number = 0
tot = 0;
print("Please wait, computing...")
for root, dirs, files in os.walk(os.getcwd()):
    for file in files:
        tot += 1
        extension = file[::-1].split(".")[0][::-1]
        try:
            ind = list.index(extension)
            counter[ind] = int(counter[ind]) + 1
        except:
            number += 1
            list.append(extension)
            ind = list.index(extension)
            counter.append(1)
for i in range (0, number):
    print(list[i] + " : " + str(counter[i]))
#print(list)
print("\n\ndone, total files: " + str(tot) + "\nnumber of file types: " + str(number))