x = int(input())

# def is_leap_year(x):
if (x%4 == 0 and x%100 != 0) or (x%400 == 0):
    print('True')
else:
    print( 'False')        
