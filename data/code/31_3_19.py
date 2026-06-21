def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    stripped = hex_string.strip()
    if stripped.startswith('0x') or stripped.startswith('0X'):
        return int(stripped, 16)
    else:
        return int(stripped, 16)

if __name__ == '__main__':
    sample_values = ['0x1A', 'FF', '0x0', 'deadBEEF', '10', '0XABC']
    for sample in sample_values:
        result = hex_to_decimal(sample)
        print(f"{sample} -> {result}")