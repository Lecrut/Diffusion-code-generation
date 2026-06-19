def compare_large_integers(num1, num2):
    digits1 = list(map(int, str(num1)))
    digits2 = list(map(int, str(num2)))
    if len(digits1) > len(digits2):
        return 1
    elif len(digits1) < len(digits2):
        return -1
    for d1, d2 in zip(digits1, digits2):
        if d1 > d2:
            return 1
        elif d1 < d2:
            return -1
    return 0
if __name__ == '__main__':
    num1 = 98765432109876543210
    num2 = 12345678901234567890
    result = compare_large_integers(num1, num2)
    print(result)