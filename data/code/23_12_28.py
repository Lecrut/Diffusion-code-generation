import math

def are_floats_equal(num1, num2, tolerance=1e-09):
    return abs(num1 - num2) < tolerance
if __name__ == '__main__':
    value1 = 0.1 + 0.2
    value2 = 0.3
    result = are_floats_equal(value1, value2)
    print(result)