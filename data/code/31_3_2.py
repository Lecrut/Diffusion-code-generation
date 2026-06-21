def hex_to_decimal(hex_string: str) -> int:
    clean_hex = hex_string.strip()
    if clean_hex.startswith("0x") or clean_hex.startswith("0X"):
        return int(clean_hex, 16)
    return int(clean_hex, 16)

if __name__ == '__main__':
    sample_values = ["0x1A", "2F", "0XFF", "10"]
    results = []
    for value in sample_values:
        decimal_value = hex_to_decimal(value)
        results.append(decimal_value)
        print(f"{value} -> {decimal_value}")
    print(results)