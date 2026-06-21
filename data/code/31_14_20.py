def hex_to_dec(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("Empty string provided")
    
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    
    if not hex_string:
        raise ValueError("No digits provided")
    
    hex_digits = "0123456789abcdefABCDEF"
    for char in hex_string:
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    
    result = 0
    power = 0
    for i in range(len(hex_string) - 1, -1, -1):
        char = hex_string[i]
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            value = 0
        result += value * (16 ** power)
        power += 1
    
    if negative:
        result = -result
    
    return result

if __name__ == '__main__':
    sample_hex_1 = "1A3F"
    sample_hex_2 = "0x7B"
    sample_hex_3 = "-FF"
    
    print(hex_to_dec(sample_hex_1))
    print(hex_to_dec(sample_hex_2))
    print(hex_to_dec(sample_hex_3))