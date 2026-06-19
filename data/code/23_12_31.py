def are_floats_equal(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

if __name__ == '__main__':
    num1 = 0.1 + 0.2
    num2 = 0.3
    result = are_floats_equal(num1, num2)
    print(result)