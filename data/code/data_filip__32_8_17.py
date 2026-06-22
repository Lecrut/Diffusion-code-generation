def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    value = int(binary_string, 2)
    hex_string = format(value, 'x')
    return hex_string.upper() if hex_string else "0"

if __name__ == '__main__':
    test_cases = ["0", "1", "1010", "1111", "10000", "00010101", "1111000011110000"]
    for case in test_cases:
        print(binary_to_hex(case))