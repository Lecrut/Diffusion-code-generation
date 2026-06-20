NUM1 = 5
NUM2 = 3

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
if __name__ == '__main__':
    result_add = add(NUM1, NUM2)
    result_subtract = subtract(10, NUM2)
    print(f'Addition: {result_add}')
    print(f'Subtraction: {result_subtract}')