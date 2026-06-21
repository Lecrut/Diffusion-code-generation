def binary_to_hexadecimal(binary_string: str) -> str:
    if not binary_string:
        return "0"
    
    decimal_value = 0
    length = len(binary_string)
    
    for char in binary_string:
        decimal_value = (decimal_value << 1) | int(char)
        
    if decimal_value == 0:
        return "0"
        
    hex_digits = []
    while decimal_value > 0:
        remainder = decimal_value & 0xF
        if remainder < 10:
            hex_digits.append(str(remainder))
        else:
            hex_digits.append(chr(ord('a') + (remainder - 10)))
        decimal_value >>= 4
        
    return "".join(reversed(hex_digits))

if __name__ == '__main__':
    sample_inputs = ["0001", "11111111", "10101010", "0", "1111111111111111"]
    for s in sample_inputs:
        result = binary_to_hexadecimal(s)
        print(result)