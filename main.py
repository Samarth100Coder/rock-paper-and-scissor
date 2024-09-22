import random
choice=random.choice(['rock','paper','scissor'])
user=input('type either rock, paper or scissor: ')
print('Computer: ',choice)
print('User: ',user)
if choice==user:
    print('It is a tie')
elif user=='rock':
    if choice=='paper':
        print('Computer wins')
    else:
        print('User wins')
elif user=='paper':
    if choice=='scissor':
        print('Computer wins')
    else:
        print('User wins')
else:
    if choice=='scissor':
        print('Computer wins')
    else:
        print('User wins')