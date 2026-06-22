def int_to_binary(n):
    if n == 0:
        return '0'
    
    negative = False
    if n < 0:
        negative = True
        n = -n
    
    binary_digits = []
    while n > 0:
        binary_digits.append(str(n & 1))
        n >>= 1
    
    binary_digits.reverse()
    result = ''.join(binary_digits)
    
    if negative:
        result = '-' + result
    
    return result

if __name__ == '__main__':
    sample_value = 1024
    result = int_to_binary(sample_value)
    print(result)
    
    sample_value_large = 123456789012345678901234567890
    result_large = int_to_binary(sample_value_large)
    print(result_large)
    
    sample_negative = -42
    result_neg = int_to_binary(sample_negative)
    print(result_neg)