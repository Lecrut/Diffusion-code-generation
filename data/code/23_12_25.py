def are_floats_equal(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) < tolerance

if __name__ == '__main__':
    float_a = 0.1 + 0.2
    float_b = 0.3
    result = are_floats_equal(float_a, float_b)
    print(result)