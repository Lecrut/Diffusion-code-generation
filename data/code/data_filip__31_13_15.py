def hex_to_decimal(hex_string: str) -> int:
    result = 0
    for char in hex_string:
        result <<= 4
        if '0' <= char <= '9':
            result |= ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            result |= ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            result |= ord(char) - ord('A') + 10
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    decimal_value = hex_to_decimal(sample_hex)
    print(decimal_value)

    sample_hex2 = "FF"
    decimal_value2 = hex_to_decimal(sample_hex2)
    print(decimal_value2)

    sample_hex3 = "0"
    decimal_value3 = hex_to_decimal(sample_hex3)
    print(decimal_value3)