def check_difference(a, b):
    return a != b
if __name__ == '__main__':
    num1 = 10
    num2 = 10
    result1 = check_difference(num1, num2)
    print(f"Difference between {num1} and {num2}: {result1}")
    num3 = 5
    num4 = 8
    result2 = check_difference(num3, num4)
    print(f"Difference between {num3} and {num4}: {result2}")
    num5 = -3.5
    num6 = -3.5000000000000004
    result3 = check_difference(num5, num6)
    print(f"Difference between {num5} and {num6}: {result3}")