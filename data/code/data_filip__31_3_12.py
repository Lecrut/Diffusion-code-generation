def hex_to_decimal(hex_str):
    if isinstance(hex_str, str):
        hex_str = hex_str.strip()
        if hex_str.startswith('0x') or hex_str.startswith('0X'):
            base = 16
            val = int(hex_str[2:], base)
        else:
            base = 16
            val = int(hex_str, base)
    else:
        val = int(str(hex_str), 16)
    return val

if __name__ == '__main__':
    results = []
    samples = ['0x1A', 'FF', '0x0', '255', '0X10', '10']
    for s in samples:
        val = hex_to_decimal(s)
        results.append(val)
    for r in results:
        print(r)