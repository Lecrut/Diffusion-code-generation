def hex_to_decimal(value):
    if isinstance(value, str):
        if value.startswith('0x') or value.startswith('0X'):
            value = value[2:]
        return int(value, 16)
    return int(value)

if __name__ == '__main__':
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('10A'))
    print(hex_to_decimal(255))