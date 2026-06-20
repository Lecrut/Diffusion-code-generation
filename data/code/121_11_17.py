def compare_integers(a, b):
    if a > b:
        return (1, 0)
    elif a < b:
        return (0, 1)
    else:
        return (1, 1)

if __name__ == '__main__':
    num1 = 56789
    num2 = 98765
    result1 = compare_integers(num1, num2)
    print(result1)
    num3 = 456789
    num4 = 456789
    result2 = compare_integers(num3, num4)
    print(result2)