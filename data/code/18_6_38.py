def compare_large_integers(num1, num2):
    if isinstance(num1, str) and isinstance(num2, str):
        return compare_string_numbers(num1, num2)
    
    if num1 > num2:
        return 1
    elif num1 < num2:
        return -1
    else:
        return 0

def compare_string_numbers(str_num1, str_num2):
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
    number1 = 987654321098765432109876543210
    number2 = 123456789012345678901234567890
    result = compare_large_integers(number1, number2)
    print(result)

    str_number1 = '12345678901234567890'
    str_number2 = '1234567890123456789'
    result_str = compare_large_integers(str_number1, str_number2)
    print(result_str)