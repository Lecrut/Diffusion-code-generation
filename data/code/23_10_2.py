import math
def compare_floats(a, b, tolerance):
    difference = math.fabs(a - b)
    return difference <= tolerance
if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    tolerance = 1e-9
    result = compare_floats(num1, num2, tolerance)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Tolerance: {tolerance}")
    print(f"Are the numbers equal within tolerance? {result}")