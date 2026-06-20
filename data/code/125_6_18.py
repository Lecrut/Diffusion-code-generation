NUM1 = 50
NUM2 = 30

def perform_addition(x, y):
    return x + y

def perform_subtraction(x, y):
    return x - y
if __name__ == '__main__':
    result_add = perform_addition(NUM1, NUM2)
    print(f'Addition Result: {result_add}')
    result_subtract = perform_subtraction(NUM1, NUM2)
    print(f'Subtraction Result: {result_subtract}')