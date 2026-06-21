def binary_to_hex(binary_string):
    binary_string = binary_string.strip()
    if not binary_string:
        return ""
    hex_digits = "0123456789abcdef"
    result = []
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i + 4]
        chunk = chunk.zfill(4)[-4:]
        decimal_value = int(chunk, 2)
        hex_char = hex_digits[decimal_value]
        result.append(hex_char)
    return "".join(result)

if __name__ == '__main__':
    sample_binary = "1111000010101010"
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)