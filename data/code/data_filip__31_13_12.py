def hex_to_decimal(hex_input: str) -> int:
    result = 0
    for char in hex_input:
        result = result << 4
        if '0' <= char <= '9':
            result |= ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            result |= ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            result |= ord(char) - ord('A') + 10
        else:
            raise ValueError(f'Invalid hexadecimal digit: {char}')
    return result
if __name__ == '__main__':
    hex_string = '1A3F'
    decimal_value = hex_to_decimal(hex_string)
    print(decimal_value)