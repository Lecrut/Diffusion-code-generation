def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:]
    if not hex_string:
        return "0"
    return hex_string.upper()

if __name__ == '__main__':
    binary_strings = ["0", "0000", "1010", "11111111", "10010111"]
    for binary in binary_strings:
        print(binary_to_hex(binary))