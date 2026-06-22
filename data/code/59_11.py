def digit_sum(n: int) -> int:
    if n < 0:
        n = -n
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    large_number = 123456789012345678
    result = digit_sum(large_number)
    print(result)
    
    test_val = 999999999999999999
    print(digit_sum(test_val))
    
    negative_test = -1000000000000000001
    print(digit_sum(negative_test))