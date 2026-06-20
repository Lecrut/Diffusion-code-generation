def compare_large_integers(a, b):
    if a > b:
        return (1, 0)
    elif b > a:
        return (0, 1)
    else:
        return (0, 0)

if __name__ == '__main__':
    num1 = 12345678901234567890
    num2 = 12345678901234567891
    result = compare_large_integers(num1, num2)
    print(result)

    num3 = 98765432109876543210
    num4 = 98765432109876543210
    result = compare_large_integers(num3, num4)
    print(result)

    num5 = 55555555555555555555
    num6 = 44444444444444444444
    result = compare_large_integers(num5, num6)
    print(result)