def reverse_binary_conversion(number):
    if number == 0:
        return '0'
    if number < 0:
        return '-' + reverse_binary_conversion(-number)
    
    bits = []
    n = number
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    
    return ''.join(reversed(bits))

if __name__ == '__main__':
    sample_number = 42
    result = reverse_binary_conversion(sample_number)
    print(result)
    
    sample_number_neg = -13
    result_neg = reverse_binary_conversion(sample_number_neg)
    print(result_neg)
    
    sample_zero = 0
    result_zero = reverse_binary_conversion(sample_zero)
    print(result_zero)