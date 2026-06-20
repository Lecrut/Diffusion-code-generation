def validate_number(value):
    if not isinstance(value, (int, float)):
        raise ValueError('Input must be a number')

def add(a, b):
    validate_number(a)
    validate_number(b)
    return a + b

def subtract(a, b):
    validate_number(a)
    validate_number(b)
    return a - b
if __name__ == '__main__':
    result_add = add(5, 3)
    result_subtract = subtract(10, 4)
    print(result_add)
    print(result_subtract)