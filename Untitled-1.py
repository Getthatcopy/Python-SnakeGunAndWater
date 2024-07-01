'''
1 for snake
-1 for water
0 for gun
'''
computer = -1
youStr = input("Enter your choice: ")
youDict = {"s": 1,
           "w" : -1,
           "g" : 0
           }
you  = youDict[youStr]
if(computer == you)
print("DRAW")
else :
 if(computer==-1 and you ==1):
    print("You Win!")
 if(computer==-1 and you ==0):
    print("You Lose!")
 if(computer==1 and you ==-1):
    print("You Lose")
 if(computer==1 and you ==0):
    print("You Win")
 if(computer==0 and you ==1):
    print("You Win")
 if(computer==0 and you ==-1):
    print("You Lose")
 else:
    print("Something went wrong")