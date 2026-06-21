def hex_to_decimal(hex_str):
    if isinstance(hex_str, str):
        if hex_str.startswith('0x') or hex_str.startswith('0X'):
            return int(hex_str[2:], 16)
        else:
            return int(hex_str, 16)
    else:
        raise TypeError("Input must be a string")

if __name__ == '__main__':
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('1A'))
    print(hex_to_decimal('0x10'))