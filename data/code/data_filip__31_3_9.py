def hex_to_decimal(hex_string: str) -> int:
    normalized = hex_string.strip().lower()
    if normalized.startswith('0x'):
        return int(normalized, 16)
    else:
        return int(normalized, 16)

if __name__ == '__main__':
    sample_1 = '0x1a'
    sample_2 = 'ff'
    sample_3 = '0XDEAD'
    result_1 = hex_to_decimal(sample_1)
    result_2 = hex_to_decimal(sample_2)
    result_3 = hex_to_decimal(sample_3)
    print(result_1)
    print(result_2)
    print(result_3)