OP_ADD = 'add'
OP_SUBTRACT = 'subtract'

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    result_subtract = subtract(num1, num2)
    print(f'Addition: {result_add}')
    print(f'Subtraction: {result_subtract}')