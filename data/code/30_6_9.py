def decimal_to_binary(decimal):
    if decimal == 0:
        return '0'
    
    is_negative = decimal < 0
    decimal = abs(decimal)
    
    bits = []
    while decimal > 0:
        bits.append(str(decimal % 2))
        decimal = decimal >> 1
    
    bits.reverse()
    result = ''.join(bits)
    
    if is_negative:
        result = '-' + result
    
    return result

if __name__ == '__main__':
    sample_values = [0, 10, -15, 255, 1]
    for val in sample_values:
        print(decimal_to_binary(val))