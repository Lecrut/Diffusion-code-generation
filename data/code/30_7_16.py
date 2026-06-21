def decimal_to_binary(n):
    if n == 0:
        return '0b0'
    if n == 1:
        return '0b1'
    
    result = []
    abs_n = abs(n)
    while abs_n > 0:
        remainder = abs_n % 2
        result.append(str(remainder))
        abs_n = abs_n // 2
    
    result.reverse()
    binary_str = ''.join(result)
    
    if n < 0:
        return '-0b' + binary_str
    
    return '0b' + binary_str

if __name__ == '__main__':
    test_values = [0, 1, 10, -5, 255]
    for val in test_values:
        print(decimal_to_binary(val))