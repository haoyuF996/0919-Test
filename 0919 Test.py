def Task1():
    char = input('A character to replace all spaces:')#string
    ori_text = open('qbdata.txt','r').readlines()#list of string
    new_text = []#list
    for line in ori_text:
        pre_index = 0#integer
        count = 0#integer
        NewLine = ''#string
        while count<len(line):
            if line[count] == ' 'or line[count] == '\n':
                NewLine += line[pre_index:count]
                NewLine += char
                pre_index =  count+1
            count+=1
        new_text.append(NewLine[:-1]+'\n')
    handle = open('qbdata.txt','w')#file handle
    for newline in new_text:
        handle.write(newline)
def Task2():
    name = input('Name to be removed:')
    ori_text = open('qbdata.txt','r').readlines()#list of string
    handle = open('qbdata_new.txt','w')#file handle
    ID = 0#integer
    for line in ori_text:
        write = True#Boolen
        count = 0#integer
        while count<len(line):
            if line[:count] == name:
                write = False
            count+=1
        if write:
            zeros = '0'*(4-len(str(ID)))#string
            handle.write(zeros+str(ID)+' '+line)
            ID+=1
    handle.close()
def Task3():
    ID = input('Please input a four digit code:')#string
    text = open('qbdata_new.txt','r').readlines()#list of string
    found = False#Boolen
    for line in text:
        if line[:4]==ID:
            found = True
            print(line)
    if not found:
        print('Data Not Found')
if __name__ == "__main__":
    choice = int(input('Task to be runed(1/2/3):'))
    if choice==1:
        Task1()
    elif choice==2:
        Task2()
    else:
        Task3()
