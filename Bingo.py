#AQA skeleton code 2020 developed by JK project Team.

import random

print("\n"*100)

phraselist = ["I'm just going to take over your machines","Coat(s) off","Is Cian in today?","I haven't had time to mark your work","I haven't learnt C# yet","I can't hear you Martin","How's Waitrose?","Saun","What are you doing for your NEA?","Where's your homework?","You should know this","We've covered this","I don't think this is complex enough","My year 7s can do this","My year 13s still can't conrmalise databases","If you can't do this by now, we have an issue","Jamie could you help Jack?","Right!","Well you better fix it then!","Back when I was in Uni we didn't have computers","What have you done?!","It's on the classroom","I have shared it with you"]
datalist = []

for i in range(9):
    data = random.randint(0,22)
    phrase = phraselist[data]
    datalist.append(phrase)

c = 1

for each in datalist:
    amount = 35-len(each)
    print(" "*amount, end="")
    if c in [3,6,9]:
        endline = "\n"*2
    else:
        endline = " "*amount
    print(each, end=endline)
    c += 1

#Contributed to by J and K.
