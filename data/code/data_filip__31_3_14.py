def hex_to_decimal(hex_string):
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        return int(hex_string, 16)
    return int(hex_string, 16)

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x0'))
    print(hex_to_decimal('10'))