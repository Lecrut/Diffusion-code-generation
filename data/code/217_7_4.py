def compare_numbers(a, b):
    if a > b:
        return {'larger': a, 'smaller': b, 'equal': None}
    elif b > a:
        return {'larger': b, 'smaller': a, 'equal': None}
    else:
        return {'larger': a, 'smaller': b, 'equal': True}
if __name__ == '__main__':
    num1 = 15
    num2 = 7
    result1 = compare_numbers(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 22
    num4 = 22
    result2 = compare_numbers(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 5
    num6 = 100
    result3 = compare_numbers(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")