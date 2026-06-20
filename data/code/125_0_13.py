def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    num1 = 15
    num2 = 27
    result_add = add(num1, num2)
    print(f'Addition result: {result_add}')
    result_subtract = subtract(num1, num2)
    print(f'Subtraction result: {result_subtract}')