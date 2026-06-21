def hex_to_decimal(hex_str):
    cleaned = hex_str.strip()
    if cleaned.startswith('0x') or cleaned.startswith('0X'):
        return int(cleaned, 16)
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal('0x1A3'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x0'))
    print(hex_to_decimal('deadBEEF'))
    print(hex_to_decimal('0X42'))