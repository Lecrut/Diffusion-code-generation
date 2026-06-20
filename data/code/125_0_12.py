def validate_int(value):
    if not isinstance(value, int):
        raise ValueError("Input must be an integer")

def add(a, b):
    validate_int(a)
    validate_int(b)
    return a + b

def subtract(a, b):
    validate_int(a)
    validate_int(b)
    return a - b

if __name__ == '__main__':
    result_add = add(15, 27)
    print(result_add)
    result_subtract = subtract(10, 4)
    print(result_subtract)