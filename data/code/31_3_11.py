def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise TypeError("Input must be a string")
    stripped = hex_string.strip()
    if stripped.lower().startswith('0x'):
        cleaned = stripped[2:]
    else:
        cleaned = stripped
    return int(cleaned, 16)

if __name__ == '__main__':
    samples = ['0x1A', 'ff', '0X0', '2F', '0xdeadbeef']
    for sample in samples:
        print(hex_to_decimal(sample))