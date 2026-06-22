def combine_checks(first, second, third):
    if not isinstance(first, int) or not isinstance(second, int) or not isinstance(third, int):
        raise ValueError("Inputs must be integers")
    if first == 0:
        raise ValueError("First input cannot be zero")
    
    is_positive = first > 0
    is_even = second % 2 == 0
    is_divisible = third % first == 0
    
    return is_positive and is_even and is_divisible

if __name__ == '__main__':
    result1 = combine_checks(4, 8, 16)
    print(result1)
    
    result2 = combine_checks(3, 5, 9)
    print(result2)
    
    result3 = combine_checks(-2, 4, 8)
    print(result3)
    
    result4 = combine_checks(2, 7, 14)
    print(result4)