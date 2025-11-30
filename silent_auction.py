print("welcome to silent auction")
#name=input("what is your name?\n")
#amount=int(input("how much you want to pay?\n"))
start="True"
winner={}
money=[]
while start=="True":
    name = input("what is your name?\n")
    amount =int(input("how much you want to pay?\n"))
    winner[name ] = amount
    money.append(amount)
    restart=input("are there any bidder?type 'yes' or 'no' ?").lower()
    if restart=='yes':
        print("\n"*100)
        print("Welcome to silent auction")
        start="True"
    else:
        start="False"
#print(winner)

max=0
for item in money:
    if item>=max:
        max=item
a=max
for i in winner:
    b=winner[i]
    if b==a :
        print(f"winner is {i}.Amount  paid is {a}")





