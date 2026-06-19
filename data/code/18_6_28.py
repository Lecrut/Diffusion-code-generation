def compare_large_integers(num1: str, num2: str) -> int:
    list1 = [int(digit) for digit in num1]
    list2 = [int(digit) for digit in num2]
    if len(list1) > len(list2):
        return 1
    elif len(list1) < len(list2):
        return -1
    for d1, d2 in zip(list1, list2):
        if d1 > d2:
            return 1
        elif d1 < d2:
            return -1
    return 0
if __name__ == '__main__':
    num1 = '12345678901234567890'
    num2 = '98765432109876543210'
    result = compare_large_integers(num1, num2)
    print(result)