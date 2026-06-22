import math

def are_floats_equal(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) < tolerance

if __name__ == '__main__':
    float1 = 0.1 + 0.2
    float2 = 0.3
    result = are_floats_equal(float1, float2)
    print(result)