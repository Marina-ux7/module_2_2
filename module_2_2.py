first=int(input("First: "))
second=int(input("Second: "))
third=int(input("Third: "))
if first==second==third:
    print('3')
elif second==first or second==third:
    print('2')
elif third==first or third==second:
    print('2')
else:
    print('0')