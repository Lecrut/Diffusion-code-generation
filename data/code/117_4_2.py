def calculate_absolute_difference(a, b):
    return abs(a - b)
if __name__ == '__main__':
    num1 = 10
    num2 = -5
    result1 = calculate_absolute_difference(num1, num2)
    print(f"The absolute difference between {num1} and {num2} is: {result1}")
    num3 = -20
    num4 = 15
    result2 = calculate_absolute_difference(num3, num4)
    print(f"The absolute difference between {num3} and {num4} is: {result2}")
    num5 = 7
    num6 = 3
    result3 = calculate_absolute_difference(num5, num6)
    print(f"The absolute difference between {num5} and {num6} is: {result3}")