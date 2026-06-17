import math
def compare_and_difference(a, b):
    if abs(a - b) < 1e-9:
        return 0.0
    else:
        return a - b
if __name__ == '__main__':
    num1 = 1.0000000000000001
    num2 = 1.0
    diff1 = compare_and_difference(num1, num2)
    print(f"Difference between {num1} and {num2}: {diff1}")
    num3 = 3.14159
    num4 = 3.1415926535
    diff2 = compare_and_difference(num3, num4)
    print(f"Difference between {num3} and {num4}: {diff2}")
    num5 = 5.0
    num6 = 5.0
    diff3 = compare_and_difference(num5, num6)
    print(f"Difference between {num5} and {num6}: {diff3}")