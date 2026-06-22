def binary_to_hexadecimal(binary_string):
    if not binary_string:
        return '0'
    
    hex_chars = '0123456789abcdef'
    result = []
    
    length = len(binary_string)
    remainder = length % 4
    
    if remainder != 0:
        padding = '0' * (4 - remainder)
        binary_string = padding + binary_string
    
    length = len(binary_string)
    
    for i in range(0, length, 4):
        nibble = 0
        chunk = binary_string[i:i+4]
        
        if chunk[0] == '1':
            nibble |= 8
        if chunk[1] == '1':
            nibble |= 4
        if chunk[2] == '1':
            nibble |= 2
        if chunk[3] == '1':
            nibble |= 1
            
        result.append(hex_chars[nibble])
    
    result_str = ''.join(result)
    
    leading_zeros_removed = []
    started = False
    for char in result_str:
        if char != '0':
            started = True
        if started:
            leading_zeros_removed.append(char)
    
    if not leading_zeros_removed:
        return '0'
        
    return ''.join(leading_zeros_removed)

if __name__ == '__main__':
    sample_inputs = ['1010', '11111111', '00001010', '', '1']
    
    for b in sample_inputs:
        print(binary_to_hexadecimal(b))