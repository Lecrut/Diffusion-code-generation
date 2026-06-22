def compare_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Both inputs must be integers.")
    
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
    
    return str_a == str_b

if __name__ == '__main__':
    print(compare_numbers(123456789, 1234567))
    print(compare_numbers(1234567, 123456789))
    print(compare_numbers(123456789, 123456789))