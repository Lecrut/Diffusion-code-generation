def compare_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both inputs must be integers.")
    
    len_a = len(str(a))
    len_b = len(str(b))
    
    max_len = max(len_a, len_b)
    
    a_str = str(a).zfill(max_len)
    b_str = str(b).zfill(max_len)
    
    for i in range(max_len):
        if a_str[i] > b_str[i]:
            return True
        elif a_str[i] < b_str[i]:
            return False
    
    return False

if __name__ == '__main__':
    print(compare_numbers(12345, 1234))
    print(compare_numbers(123456789, 12345678))
    print(compare_numbers(1234, 123456789))
    try:
        compare_numbers(1234, "1234")
    except TypeError as e:
        print(f"Error caught: {e}")