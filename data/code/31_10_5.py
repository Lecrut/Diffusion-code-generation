def hex_to_decimal(hex_string: str) -> int:
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_hex_values = ["1A", "FF", "100", "deadbeef", "0"]
    for hex_val in sample_hex_values:
        result = hex_to_decimal(hex_val)
        print(f"{hex_val} -> {result}")