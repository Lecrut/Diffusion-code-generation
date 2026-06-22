MAX_DIGIT = '9'

def compare_digit(left, right):
    if left > right:
        return 1
    elif left < right:
        return -1
    else:
        return 0

def compare_numbers(a, b):
    str_a, str_b = str(a), str(b)
    
    len_diff = len(str_a) - len(str_b)
    
    if len_diff > 0:
        for _ in range(len_diff):
            if str_a[0] != '0':
                return 1
            else:
                str_a = str_a[1:]
    elif len_diff < 0:
        for _ in range(-len_diff):
            if str_b[0] != '0':
                return -1
            else:
                str_b = str_b[1:]
    
    min_len = min(len(str_a), len(str_b))
    
    for i in range(min_len):
        digit_comparison = compare_digit(str_a[i], str_b[i])
        if digit_comparison != 0:
            return digit_comparison
    
    return compare_digit(len(str_a), len(str_b))

if __name__ == '__main__':
    print(compare_numbers(12345678901234567890, 12345678901234567891))
    print(compare_numbers(999999999999999999, 1000000000000000000))
    print(compare_numbers(1000000000000000000, 999999999999999999))
    print(compare_numbers(0, 0))