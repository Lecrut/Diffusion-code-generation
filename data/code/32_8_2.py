def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    clean_binary = binary_string.lstrip("0")
    if not clean_binary:
        return "0"
    decimal_value = int(clean_binary, 2)
    hex_value = hex(decimal_value)[2:]
    return hex_value.upper()

if __name__ == "__main__":
    test_cases = [
        "1010",
        "00011110",
        "11111111",
        "0000",
        "1",
        "11110110101111001010"
    ]
    for case in test_cases:
        result = binary_to_hex(case)
        print(result)