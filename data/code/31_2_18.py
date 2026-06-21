def hex_to_decimal(hex_str: str) -> int:
    hex_str = hex_str.strip()
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    if hex_str.startswith('#'):
        hex_str = hex_str[1:]
    is_negative = False
    if hex_str.startswith('-') or hex_str.startswith('+'):
        if hex_str.startswith('-'):
            is_negative = True
            hex_str = hex_str[1:]
        elif hex_str.startswith('+'):
            hex_str = hex_str[1:]
    hex_str = hex_str.lstrip('0') or '0'
    result = 0
    for char in hex_str:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f'Invalid hexadecimal digit: {char}')
        result = result * 16 + digit
    return -result if is_negative else result
if __name__ == '__main__':
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('10'))
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('1A'))
    print(hex_to_decimal('ff'))
    print(hex_to_decimal('abc123'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('0000'))
    print(hex_to_decimal('-FF'))
    print(hex_to_decimal('+10'))