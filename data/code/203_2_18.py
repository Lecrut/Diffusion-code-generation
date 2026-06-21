def almost_equal(num1, num2, tolerance=1e-9):
    return abs(num1 - num2) <= tolerance

if __name__ == '__main__':
    sample_values = [3.141592653589793, 3.1415926535897931, 2.718281828459045, 2.71828182845904]
    result1 = almost_equal(sample_values[0], sample_values[1])
    result2 = almost_equal(sample_values[2], sample_values[3])
    print(f"Comparing {sample_values[0]} and {sample_values[1]}: {result1}")
    print(f"Comparing {sample_values[2]} and {sample_values[3]}: {result2}")