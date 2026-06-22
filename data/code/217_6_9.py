def compare_numbers(a, b):
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both inputs must be strings representing integers.")
    
    len_a = len(a)
    len_b = len(b)
    
    if len_a > len_b:
        return True
    elif len_a < len_b:
        return False
    
    for i in range(len_a):
        if a[i] > b[i]:
            return True
        elif a[i] < b[i]:
            return False
    
    return False

if __name__ == '__main__':
    print(compare_numbers("1234567890", "123456789"))
    print(compare_numbers("123456789", "1234567890"))
    print(compare_numbers("1234567890", "12345678901"))