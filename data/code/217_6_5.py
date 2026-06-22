def compare_numbers(a, b):
    len_a = len(str(a))
    len_b = len(str(b))
    
    if len_a > len_b:
        return True
    elif len_a < len_b:
        return False
    
    for i in range(len_a):
        digit_a = int(str(a)[i])
        digit_b = int(str(b)[i])
        
        if digit_a > digit_b:
            return True
        elif digit_a < digit_b:
            return False
    
    return False

if __name__ == '__main__':
    print(compare_numbers(12345, 6789))
    print(compare_numbers(98765, 12345))
    print(compare_numbers(56789, 56789))