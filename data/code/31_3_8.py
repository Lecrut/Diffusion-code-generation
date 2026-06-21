def hex_to_decimal(hex_str):
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        return int(hex_str, 16)
    return int(hex_str, 16)

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x100'))