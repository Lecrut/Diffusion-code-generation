NUM1 = 20
NUM2 = 8

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    sum_result = add(NUM1, NUM2)
    difference_result = subtract(NUM1, NUM2)
    print(f"Sum: {sum_result}")
    print(f"Difference: {difference_result}")