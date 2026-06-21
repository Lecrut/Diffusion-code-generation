def hex_to_decimal(hex_string):
    clean_hex = hex_string
    if clean_hex.startswith('0x') or clean_hex.startswith('0X'):
        clean_hex = clean_hex[2:]
    return int(clean_hex, 16)

if __name__ == '__main__':
    samples = ['0x1A', '2F', '0XFF', 'ABC', '0x0']
    for s in samples:
        print(hex_to_decimal(s))