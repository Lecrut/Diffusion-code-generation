def compare_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers.")
    
    str_a = str(a)
    str_b = str(b)
    len_a = len(str_a)
    len_b = len(str_b)
    
    min_len = min(len_a, len_b)
    
    for i in range(min_len):
        if str_a[i] != str_b[i]:
            return int(str_a[i]) > int(str_b[i])
    
    return len_a > len_b

if __name__ == '__main__':
    print(compare_numbers(5, 3))
    print(compare_numbers(5.0, 3))
    print(compare_numbers(123, 4567))
    print(compare_numbers(123.456, 123.455))