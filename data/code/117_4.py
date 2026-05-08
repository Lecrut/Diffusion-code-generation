def calculate_absolute_difference(a, b):
    return abs(a - b)
if __name__ == '__main__':
    num1 = 10
    num2 = -5
    result1 = calculate_absolute_difference(num1, num2)
    print(f"Absolute difference between {num1} and {num2}: {result1}")
    num3 = -15
    num4 = 7
    result2 = calculate_absolute_difference(num3, num4)
    print(f"Absolute difference between {num3} and {num4}: {result2}")
    num5 = -100
    num6 = -50
    result3 = calculate_absolute_difference(num5, num6)
    print(f"Absolute difference between {num5} and {num6}: {result3}")