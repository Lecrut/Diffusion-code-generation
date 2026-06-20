NUM1 = 10
NUM2 = 5

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError('Cannot divide by zero')
    return a / b
if __name__ == '__main__':
    sum_result = add(NUM1, NUM2)
    diff_result = subtract(NUM1, NUM2)
    prod_result = multiply(NUM1, NUM2)
    quot_result = divide(NUM1, NUM2)
    print(f'Number 1: {NUM1}')
    print(f'Number 2: {NUM2}')
    print(f'Sum: {sum_result}')
    print(f'Difference: {diff_result}')
    print(f'Product: {prod_result}')
    print(f'Quotient: {quot_result}')