def compare_and_difference(a, b):
    difference = a - b
    return difference
if __name__ == '__main__':
    num1 = 3.1415926535
    num2 = 3.1415926536
    result1 = compare_and_difference(num1, num2)
    print(f"Difference between {num1} and {num2}: {result1}")
    num3 = 0.1 + 0.2
    num4 = 0.3
    result2 = compare_and_difference(num3, num4)
    print(f"Difference between {num3} and {num4}: {result2}")
    num5 = 1.0
    num6 = 0.9999999999999999
    result3 = compare_and_difference(num5, num6)
    print(f"Difference between {num5} and {num6}: {result3}")