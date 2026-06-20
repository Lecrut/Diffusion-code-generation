PRECISION = 1e-10

def subtract_floats(a, b):
    difference = a - b
    if abs(difference) < PRECISION:
        return 0.0
    return difference
if __name__ == '__main__':
    result = subtract_floats(3.141592653589793, 2.718281828459045)
    print(result)