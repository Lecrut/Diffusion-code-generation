def validate_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")

def compare_numbers_by_digits(a, b):
    str_a = str(a)
    str_b = str(b)
    
    max_len = max(len(str_a), len(str_b))
    for i in range(max_len):
        digit_a = int(str_a[i]) if i < len(str_a) else 0
        digit_b = int(str_b[i]) if i < len(str_b) else 0
        
        if digit_a > digit_b:
            return True
        elif digit_a < digit_b:
            return False
    
    return False

if __name__ == '__main__':
    validate_numbers(12345, 6789)
    print(compare_numbers_by_digits(12345, 6789))
    print(compare_numbers_by_digits(12345, 12345))
    print(compare_numbers_by_digits(12345, 54321))