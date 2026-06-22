def compare_integers(a, b):
    if a < b:
        return f"{a} is less than {b}"
    elif a > b:
        return f"{a} is greater than {b}"
    else:
        return f"{a} is equal to {b}"

if __name__ == '__main__':
    num1 = 5
    num2 = 10
    result = compare_integers(num1, num2)
    print(result)

    num3 = -3
    num4 = 7
    result2 = compare_integers(num3, num4)
    print(result2)

    num5 = 42
    num6 = 42
    result3 = compare_integers(num5, num6)
    print(result3)