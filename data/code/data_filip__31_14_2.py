def hex_to_dec(hex_string: str) -> int:
    hex_string = hex_string.strip()
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    
    decimal_value = 0
    length = len(hex_string)
    for i, char in enumerate(hex_string):
        pos = length - 1 - i
        digit = 0
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
        decimal_value += digit * (16 ** pos)
    
    if negative:
        return -decimal_value
    return decimal_value

if __name__ == '__main__':
    result = hex_to_dec('1A3F')
    print(result)
    result_negative = hex_to_dec('-FF')
    print(result_negative)