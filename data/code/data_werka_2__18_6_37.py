def compare_large_integers(num1, num2):
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

if __name__ == '__main__':
    a = 987654321098765432109876543210
    b = 123456789012345678901234567890
    result = compare_large_integers(a, b)
    print(result)