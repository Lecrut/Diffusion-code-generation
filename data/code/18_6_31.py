def compare_large_integers(a, b):
    str_a = str(a)
    str_b = str(b)
    if len(str_a) > len(str_b):
        return 1
    elif len(str_a) < len(str_b):
        return -1
    for i in range(len(str_a)):
        if str_a[i] > str_b[i]:
            return 1
        elif str_a[i] < str_b[i]:
            return -1
    return 0
if __name__ == '__main__':
    a = 987654321098765432109876543210
    b = 123456789012345678901234567890
    result = compare_large_integers(a, b)
    print(result)