def hex_to_decimal(hex_string):
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        return int(hex_string, 16)
    else:
        return int(hex_string, 16)

if __name__ == '__main__':
    samples = ['0x1A', 'FF', '0x0', 'deadBEEF', '10', '0x1a2b3c']
    for sample in samples:
        print(hex_to_decimal(sample))