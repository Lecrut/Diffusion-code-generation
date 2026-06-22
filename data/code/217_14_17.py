def compare_numbers(a, b):
    if a > b:
        return f"{a} is greater than {b}"
    elif a < b:
        return f"{a} is less than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result1 = compare_numbers(num1, num2)
    print(result1)

    num3 = -3
    num4 = 7
    result2 = compare_numbers(num3, num4)
    print(result2)

    num5 = 42
    num6 = 42
    result3 = compare_numbers(num5, num6)
    print(result3)