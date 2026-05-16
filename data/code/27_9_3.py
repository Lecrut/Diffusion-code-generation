def compare_numbers(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
if __name__ == '__main__':
    num1 = 10
    num2 = 5
    result1 = compare_numbers(num1, num2)
    print(f"Comparing {num1} and {num2}: {result1}")
    num3 = 20
    num4 = 20
    result2 = compare_numbers(num3, num4)
    print(f"Comparing {num3} and {num4}: {result2}")
    num5 = 3
    num6 = 7
    result3 = compare_numbers(num5, num6)
    print(f"Comparing {num5} and {num6}: {result3}")