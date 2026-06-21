def binary_to_hex(binary_string):
    hex_digits = '0123456789abcdef'
    hex_value = ''
    padded_binary = binary_string.zfill((len(binary_string) + 3) // 4 * 4)
    
    index = 0
    while index < len(padded_binary):
        nibble = padded_binary[index:index + 4]
        decimal_value = 0
        power = 0
        i = len(nibble) - 1
        while i >= 0:
            if nibble[i] == '1':
                decimal_value += 2 ** power
            power += 1
            i -= 1
        hex_value += hex_digits[decimal_value]
        index += 4
        
    return hex_value.lstrip('0') or '0'

if __name__ == '__main__':
    print(binary_to_hex('1101'))
    print(binary_to_hex('11111111'))
    print(binary_to_hex('0'))