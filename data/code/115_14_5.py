DIVISOR = 3.0

def divide_and_print(dividend):
    result = dividend / DIVISOR if DIVISOR != 0 else 'Division by zero'
    print(result)

if __name__ == '__main__':
    divide_and_print(150.75)