def hex_to_decimal(hex_string):
    cleaned = hex_string
    if cleaned.startswith('0x') or cleaned.startswith('0X'):
        cleaned = cleaned[2:]
    return int(cleaned, 16)

if __name__ == '__main__':
    sample_values = ['0x1A', 'FF', '0x0', '2a', '0X10', 'abc']
    results = [hex_to_decimal(s) for s in sample_values]
    print(results)