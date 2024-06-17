# brainf Code example
brainfCode = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."



loopStarts = []
loopStartCodes = {}
loopEndCodes = {}

#loop code generation
for idx, character in enumerate(brainfCode):

    if character == "[":
        loopStarts.append(idx)
        
        continue
    elif character == "]":
        openBracketLocation = loopStarts.pop()


        #start bracket codes
        endBracketLocationHex = hex(idx+1)[2:]

        startBracketCode = ""
        for _ in range(4-len(endBracketLocationHex)):
            startBracketCode += "0"
        startBracketCode += endBracketLocationHex
        startBracketCode += "0"

        loopStartCodes[openBracketLocation] = startBracketCode 


        #end bracket codes
        startBracketLocationHex = hex(openBracketLocation)[2:]

        endBracketCode = ""
        for _ in range(4-len(startBracketLocationHex)):
            endBracketCode += "0"
        endBracketCode += startBracketLocationHex
        endBracketCode += "1"

        loopEndCodes[idx] = endBracketCode


machineCode = """"""

#machine code generation
for idx, character in enumerate(brainfCode):
    if character == "+":
        machineCode += "44444"
    elif character == "-":
        machineCode += "55555"
    elif character == ">":
        machineCode += "22222"
    elif character == "<":
        machineCode += "33333"
    elif character == ".":
        machineCode += "66666"
    elif character == ",":
        machineCode += "77777"        
    elif character == "[":
        machineCode += loopStartCodes[idx]
        #print(loopStartCodes[idx])
    elif character == "]":
        machineCode += loopEndCodes[idx]
        #print(loopEndCodes[idx])
    machineCode += "\n"
    
print(machineCode)








