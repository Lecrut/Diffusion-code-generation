def hex_to_decimal(hex_str: str) -> int:
    cleaned = hex_str.strip()
    if cleaned.startswith('0x') or cleaned.startswith('0X'):
        cleaned = cleaned[2:]
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x0'))