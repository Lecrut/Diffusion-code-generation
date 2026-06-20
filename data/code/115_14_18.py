DIVISOR = 3.0

def divide(dividend):
    return dividend / DIVISOR if DIVISOR != 0 else 'Division by zero'

if __name__ == '__main__':
    result = divide(150.75)
    print(result)