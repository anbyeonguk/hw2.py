def get_integer(prompt):
    res=int(input(prompt))
    return res
def exchange(m):
     n500=m//500
     m%=500
     n100=m//100
     m%=100
     n50=m//50
     m%=50
     n10=m//10
     m%=10

  
     print('500원동전의개수',n500)
     print('100원동전의개수',n100)
     print('50원동전의개수',n50)
     print('10원동전의개수',n10)

m=get_integer('동전으로 교환하고자 하는 금액은?')
exchange(m)
