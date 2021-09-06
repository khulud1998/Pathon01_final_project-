Number_book= {'1111111111':'Amal', '2222222222':'Mohammed','3333333333':'Khadijah','4444444444':'Abdullah', '5555555555':'Rawan' ,'6666666666':'Faisal', '7777777777':'Layla'}
flag=0
while 1 :
    value11 =input('enter the number:  ')
    if len(value11) != 10 and type(value11) != int :
        print('This is invalid number')
        flag=1
    for key in Number_book :
        if value11 == key:
            print(Number_book[key])
            flag=1
    if flag == 0:
        print('Sorry, the number is not found ')
    flag=0
    key1 = input('Add number :')
    value1 = input('Add name :')
    Number_book[key1]=value1
