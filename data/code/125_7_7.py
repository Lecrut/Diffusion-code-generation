def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    x = 7
    y = 3
    result_add = add(x, y)
    result_subtract = subtract(x, y * 2)
    print("Addition Result:", result_add)
    print("Subtraction Result:", result_subtract)