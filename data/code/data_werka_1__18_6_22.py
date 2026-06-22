def compare_large_integers(num1, num2):
    str_num1 = str(num1)
    str_num2 = str(num2)
    if len(str_num1) > len(str_num2):
        return 1
    elif len(str_num1) < len(str_num2):
        return -1
    for char1, char2 in zip(str_num1, str_num2):
        if char1 > char2:
            return 1
        elif char1 < char2:
            return -1
    return 0
if __name__ == '__main__':
    num1 = 9876543210987654321098765432109876543210
    num2 = 1234567890123456789012345678901234567890
    result = compare_large_integers(num1, num2)
    print(result)