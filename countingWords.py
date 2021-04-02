string=input("Enter Your Introduction")
characterCount=0
wordCount=1
for Z in string:
    characterCount=characterCount+1
    if(Z==' '):
        wordCount=wordCount+1
        
print("Number Of Words In The Sentence:=>",wordCount)
print("Number Of Charachters In The Sentence Are:=>",characterCount)