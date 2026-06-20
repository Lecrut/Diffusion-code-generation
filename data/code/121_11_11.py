def compare_large_integers(a, b):
    if a > b:
        return (1, 0)
    elif b > a:
        return (0, 1)
    else:
        return (0, 0)

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 98765432109876543210
    result1 = compare_large_integers(num1, num2)
    print(result1)

    num3 = 11111111111111111111
    num4 = 11111111111111111111
    result2 = compare_large_integers(num3, num4)
    print(result2)

    num5 = 99999999999999999999
    num6 = 88888888888888888888
    result3 = compare_large_integers(num5, num6)
    print(result3)