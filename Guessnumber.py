import random
lie=["Dont give up","It's cold","It's near","You've gone too far mate!!","Please try harder next time","Do you have brain","Almost near dude"]
print "You wanna play a game..."
name=raw_input("What is your name?\n")
print "Thank you %s"%(name)
print "You only five tries %s"%(name)
num=random.randrange(1,15)
tries=0
tries_remaining=5
while tries < 5:
    guess=input("Choose the number which is between 1 till 15, please enter it\n")
    tries += 1
    tries_remaining -= 1
    if tries < 5:
        if guess == num:
            print random.choice(lie)
        else:
            print random.choice(lie)
    elif tries == 5:
        if guess == num:
            print "You awesome %s .. i know u can do it"%(name)
        else:
            print "Please work harder %s"%(name)
            print "The answer is %d"%(num)
    else:
        (tries == 5)
        print "%s...your brain is not working mate!!!"%(name)
        print "The answer is %d"%(num)