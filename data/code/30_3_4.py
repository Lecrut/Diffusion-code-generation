def int_to_binary(n):
    if n == 0:
        return '0'
    
    is_negative = False
    if n < 0:
        is_negative = True
        n = -n
    
    bits = []
    while n > 0:
        bits.append('1' if (n & 1) else '0')
        n >>= 1
    
    bits.reverse()
    result = ''.join(bits)
    
    if is_negative:
        result = '-' + result
    
    return result

if __name__ == '__main__':
    test_values = [0, 1, 2, 10, 255, 1024, -5, -123456789]
    for value in test_values:
        print(f"{value} -> {int_to_binary(value)}")