def binary_to_hex(binary_string: str) -> str:
    decimal_value = int(binary_string, 2)
    hex_string = hex(decimal_value)[2:]
    if len(hex_string) % 2 != 0:
        hex_string = '0' + hex_string
    return hex_string.upper()

if __name__ == '__main__':
    binary_input = "1101011011110001"
    result = binary_to_hex(binary_input)
    print(result)