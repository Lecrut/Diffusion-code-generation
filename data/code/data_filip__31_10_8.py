def hex_to_decimal(hex_string: str) -> int:
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = ['1A', 'FF', '10', 'abc', 'DEADBEEF']
    for value in sample_hex_values:
        result = hex_to_decimal(value)
        print(f"{value} -> {result}")