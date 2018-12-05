def part1():
    inputList = open("Day1/input-1.txt", "r")
    inputSum = sum(map(int, inputList))
    print (inputSum)

def part2():
    f = open("Day1/input-1.txt", "r")
    
    inputs = [int(n) for n in f.readlines()]
    foundFrequencies = set()
    curFrequencies = 0
    curIndex = 0
    while (True):        
        curInput = inputs[curIndex % len(inputs)]
        #print("CurFreq: " + str(curFrequencies) + ", CurInput: " + str(curInput))
        if(curFrequencies in foundFrequencies):
            print ("First duplicate was " + str(curFrequencies))
            return
        foundFrequencies.add(curFrequencies)
        curFrequencies = curFrequencies +  curInput        
        curIndex +=1

part2()