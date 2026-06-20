def divide_numbers(a=150.75, b=3.0):
    return a / b if b != 0 else 'Division by zero'

if __name__ == '__main__':
    print(divide_numbers())