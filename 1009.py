SELLER_NAME = input('')
FIXED_SALARY = float(input(''))
TOTAL_SALES_MONTH = float(input(''))

BONUS = TOTAL_SALES_MONTH * 0.15

TOTAL = (FIXED_SALARY + (TOTAL_SALES_MONTH * 0.15))

print('TOTAL = R$ %0.2f' %TOTAL)
