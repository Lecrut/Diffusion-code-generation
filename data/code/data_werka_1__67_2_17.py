def is_float(value):
    return isinstance(value, float)

def add_floats(a, b):
    if not (is_float(a) and is_float(b)):
        raise ValueError("Both inputs must be floating-point numbers.")
    return a + b

if __name__ == '__main__':
    num1 = 1.23456
    num2 = 9.87654
    result = add_floats(num1, num2)
    print(result)