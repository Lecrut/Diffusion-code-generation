def hex_to_decimal(hex_str: str) -> int:
    result = 0
    for char in hex_str.upper():
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = (result << 4) | value
    return result

if __name__ == '__main__':
    print(hex_to_decimal('1A3F'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('DEADBEEF'))