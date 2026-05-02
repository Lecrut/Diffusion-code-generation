import math
def calculate_ratio(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    common_divisor = math.gcd(a, b)
    return a // common_divisor, b // common_divisor
if __name__ == '__main__':
    num1 = 1234567890123456789
    num2 = 9876543210987654321
    try:
        result1, result2 = calculate_ratio(num1, num2)
        print(f"Ratio of {num1} and {num2} simplified: {result1} / {result2}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    num3 = 10000000000000000000000000000000
    num4 = 5000000000000000000000000000000
    try:
        result3, result4 = calculate_ratio(num3, num4)
        print(f"Ratio of {num3} and {num4} simplified: {result3} / {result4}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")