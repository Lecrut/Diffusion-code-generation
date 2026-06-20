def compare_integers(a, b):
    if a > b:
        return (1, 0)
    elif b > a:
        return (0, 1)
    else:
        return (0, 0)

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    result = compare_integers(num1, num2)
    print(result)

    num3 = 12345678901234567890
    num4 = 12345678901234567890
    result = compare_integers(num3, num4)
    print(result)

    num5 = 12345678901234567890
    num6 = 12345678901234567891
    result = compare_integers(num5, num6)
    print(result)