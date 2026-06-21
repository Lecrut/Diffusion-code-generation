def hex_to_decimal(hex_str):
    hex_str = hex_str.strip()
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    result = 0
    for char in hex_str:
        if '0' <= char <= '9':
            value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
        result = result * 16 + value
    return result

if __name__ == '__main__':
    print(hex_to_decimal('0A'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('1a3'))
    print(hex_to_decimal('0x1B'))
    print(hex_to_decimal('0XDeAdBeEf'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('F'))
    print(hex_to_decimal('f'))