DIVISOR = 3.0

def divide(x):
    return x / DIVISOR if DIVISOR != 0 else 'Division by zero'

if __name__ == '__main__':
    print(divide(150.75))