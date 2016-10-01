#This function is to check quality of (y/n) inputs
#It will loop until it has valid input
def getYN_in():
    checkYN='stop'
    while checkYN!='y' and checkYN!='n':  #check !='y' or check !='n'
        checkYN=input('Is the Text Above Correct?(y/n)\n')
    return checkYN

#This function is to check quality of NUMBER inputs
#If the input does not qualify, the program will not return
def getNum_in (min,max):
    hasGoodin=False
    while not hasGoodin:
        #get input as int
        numIn=int(input())
        if numIn<=max and numIn>=min:
            hasGoodin=True
    #if subjectNum>=min and subjectNum<=max:
    return numIn


print("This program will help students plan school assignments by providing steps for\n different types"
      " of assignments.\n")

print("Here are the available assignment options:\n1:Write a Paper\n2:Create a Study Guide\n"
      '3:Group Project\n4:Read a Textbook Chapter\n5:Research Paper\n')

subjectNameList=['Write a Paper','Create a Study Guide','Group Project','Read a Textbook Chapter','Research Paper']
print('Please enter the assignment by entering the corresponding number:')
#input-selecting the subject
subjectNum=getNum_in(1,len(subjectNameList)) -1 #-1 because lists count from 0
print('\n')

paperSteps=["Research", "Choose Thesis", "Outline Paper", "Write Paper", "Visit Writing Center", "Edit Paper"]
guideSteps=["Write Class Notes", "Write Reading Notes", "Label Notes by Topic", "Start Study Guide", "Add Topics Names", "Add Topic Details"]
projectSteps=['Initial Meeting With Group','Outline Project','Set Individuals Tasks','Schedule Group Meetings','Check In With Email','Edit Project','Submit Project']
bookSteps=['Read Title and Subtitle','Scan Reading','Note Vocabulary and Key Concepts',"Note Concepts You Don't Understand",'Write a Chapter Summary in Your Own Terms']
repaperSteps=['Research Topic','Choose Sources','Take Notes on Sources','Create Citations','Outline Paper','Write Paper','Edit Paper','Writing Center Visit','Final Edits']
subjectList = [paperSteps,  guideSteps, projectSteps, bookSteps, repaperSteps,]

currentSubj = subjectList[subjectNum]

numSteps=len(currentSubj)

for step in currentSubj:  #for each item in the list
    print(step)

#input yes/no "confirm"
stepsCheck=getYN_in()
if stepsCheck=='n':
    missing=input('Is there something missing?(y/n)\n')
    while missing=='y':
        newStep=input('Enter New Step: \n')
        currentSubj.append(newStep)
        missing=input('Is there anything else missing?(y/n)\n')
    for index in range(0,len(currentSubj)):
        print(index, ' ', currentSubj[index])
        
    order=input('Is the order correct?(y/n)\n')
    if order=='n':
        print('If there is a step that you would like to remove, withhold it from the order.')
        print('Enter Steps in desired order using the corresponding number.')
        print('Please enter each number with a single space seperating them: ')
        usrOrder=input(' ')
        usrOrder=usrOrder.split()
        newOrder=[]
        for num in usrOrder:
            newOrder.append(currentSubj[int(num)])
        for step in newOrder:
            print(step)
            
print('Please Enter The Numbers of Days Until Your Due Date Below:')
#input number of days away
dueDate=getNum_in(0,200)

calcDays=dueDate/numSteps

daysPassed=1
for step in currentSubj:  #for each item in the list
    daysPassed+=calcDays
    print('Complete by Day',format(daysPassed,'.2f'),'\t',step)

print(str(format(calcDays,'.2f')), "is the number of days you have to complete each step")



