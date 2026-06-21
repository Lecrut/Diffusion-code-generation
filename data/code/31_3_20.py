def hex_to_decimal(s):
    s = s.strip()
    if s.startswith('0x') or s.startswith('0X'):
        return int(s, 16)
    return int(s, 16)

if __name__ == '__main__':
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('FF'))