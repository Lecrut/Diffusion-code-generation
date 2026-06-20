calculate_difference = lambda a, b: abs(a - b)
if __name__ == '__main__':
    num1, num2 = (10, -5)
    result1 = calculate_difference(num1, num2)
    print(f'Difference between {num1} and {num2}: {result1}')
    num3, num4 = (-15, 7)
    result2 = calculate_difference(num3, num4)
    print(f'Difference between {num3} and {num4}: {result2}')