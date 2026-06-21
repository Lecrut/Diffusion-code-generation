def binary_to_hex(binary_string: str) -> str:
    hex_digits = "0123456789abcdef"
    padding_length = (4 - len(binary_string) % 4) % 4
    padded_binary = "0" * padding_length + binary_string
    hex_result = ""
    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i + 4]
        value = 0
        for bit in nibble:
            value = (value << 1) + int(bit)
        hex_result += hex_digits[value]
    return hex_result

if __name__ == '__main__':
    sample_binary = "110101101010"
    result = binary_to_hex(sample_binary)
    print(result)