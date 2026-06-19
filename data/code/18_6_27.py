def compare_large_integers(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) > len(str_num2):
        return 1
    elif len(str_num1) < len(str_num2):
        return -1
    for d1, d2 in zip(str_num1, str_num2):
        if d1 > d2:
            return 1
        elif d1 < d2:
            return -1
    return 0
if __name__ == '__main__':
    sample_value1 = 123456789012345678901234567890
    sample_value2 = 987654321098765432109876543210
    result = compare_large_integers(sample_value1, sample_value2)
    print(result)