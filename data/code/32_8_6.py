def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    normalized = binary_string.lstrip("0")
    if not normalized:
        return "0"
    decimal_value = int(normalized, 2)
    hex_string = format(decimal_value, "X")
    return hex_string

if __name__ == "__main__":
    test_cases = ["0", "1", "1010", "00011011", "111100001010", "0000"]
    for case in test_cases:
        result = binary_to_hex(case)
        print(f"{case} -> {result}")