
f = open("tester.txt", "r")
assem = []
if(f== None):
    print("error: can't open file", f)
else:
    for x in f:
        assem.append(x)
        print(x)
    f.close


machine_c = []
dec = []
label = []
opcode = []
ins = ['add', 'nand', 'lw', 'sw', 'beq', 'jalr', 'halt', 'noop']
rs = []
rt = []
rd = []

for i in range(len(assem)): #loop assemble code
    x = assem[i].split() 
    n = 0

    if x[0] in ins: #In case code doesn't have label
        if x[0] =='add':
            opcode.append('000')
        elif x[0] == 'nand':
            opcode.append('001')
        elif x[0] == 'lw':
            opcode.append('010')
        elif x[0] == 'sw':
            opcode.append('011')
        elif x[0] == 'beq':
            opcode.append('100')
        elif x[0] == 'jarl':
            opcode.append('101')
        elif x[0] == 'halt':
            opcode.append('110')
        elif x[0] == 'noop':
            opcode.append('111')
        
        label.append(None) #Set label[i] is null

    elif len(x[0]) >6 or x[0][0].isdigit() : #Check label
        print("error: Label error")
        break
    else:
        label.append(x[0])
        if x[1] =='add':
            opcode.append('000')
        elif x[1] == 'nand':
            opcode.append('001')
        elif x[1] == 'lw':
            opcode.append('010')
        elif x[1] == 'sw':
            opcode.append('011')
        elif x[1] == 'beq':
            opcode.append('100')
        elif x[1] == 'jarl':
            opcode.append('101')
        elif x[1] == 'halt':
            opcode.append('110')
        elif x[1] == 'noop':
            opcode.append('111')
        elif x[1] == '.fill':
            print("No Idea")
        n = 1


    



    # R-type
    if(opcode[i] == '000' or opcode[i] == '001'):
        rs.append(bin(int(x[n+1]))[2:].zfill(3))
        rt.append(bin(int(x[n+2]))[2:].zfill(3))
        rd.append(bin(int(x[n+3]))[2:].zfill(3)) 

        # print(rs[i],rt[i],rd[i])
        m = opcode[i]+rs[i]+rt[i]+'0000000000000'+rd[i]
        # print(m)
        
    # I-Type
    elif (opcode[i] == '010' or opcode[i] == '011' or opcode[i] == '100') :
        rs.append(bin(int(x[n+1]))[2:].zfill(3))
        rt.append(bin(int(x[n+2]))[2:].zfill(3))
        rd.append(bin(int(x[n+3]))[2:].zfill(16)) #still not 2's

        # print(rs[i],rt[i],rd[i])
        m = opcode[i]+rs[i]+rt[i]+rd[i]
        # print(m)
        
    # J-Type
    elif (opcode[i] == '101') :
        rs.append(bin(int(x[n+1]))[2:].zfill(3))
        rd.append(bin(int(x[n+2]))[2:].zfill(3))

        # print(rs[i],rt[i],rd[i])
        m = opcode[i]+rs[i]+rd[i]+'0000000000000000'
        # print(m)
    #
    # O-Type
    elif (opcode[i] == '110' or opcode[i] == '111'):
        m=opcode[i] + '0000000000000000000000'


    machine_c.append((m)) 
    decimal = int(machine_c[i], 2)
    dec.append(decimal)
    
    print(f"(address {i}): {dec[i]}" ) #print decimal of code line by line

print(label)
