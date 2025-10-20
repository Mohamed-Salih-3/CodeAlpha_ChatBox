def fun(n):
    d={'hi how are you':'i am fine what about you',
       'whats going on':'nothing just chatting'}
    dd=d.keys()
    if n in dd:
        print(d[n])
    else:
        print("sorry I dont understand")
ch=input("enter yours : ").lower()
fun(ch)