def hex_to_decimal(hex_string: str) -> int:
    return int(hex_string, 16)

if __name__ == '__main__':
    sample_values = ['FF', '1A3', '0', 'DEADBEEF', '100']
    for hex_val in sample_values:
        result = hex_to_decimal(hex_val)
        print(f"Hex {hex_val} converts to {result}")