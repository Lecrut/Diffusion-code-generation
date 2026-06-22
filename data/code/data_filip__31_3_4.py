def hex_to_decimal(hex_string: str) -> int:
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        return int(hex_string, 16)
    return int(hex_string, 16)

if __name__ == '__main__':
    test_cases = ["0xFF", "0x1A3", "FF", "1A3"]
    for case in test_cases:
        print(hex_to_decimal(case))