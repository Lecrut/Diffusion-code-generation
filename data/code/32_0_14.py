def binary_to_hex(binary_string):
    if not binary_string:
        return "0"

    padding_length = (4 - len(binary_string) % 4) % 4
    padded_binary = "0" * padding_length + binary_string

    hex_digits = "0123456789abcdef"
    hex_result = []

    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i + 4]
        decimal_value = 0
        for j, bit in enumerate(reversed(nibble)):
            if bit == '1':
                decimal_value += 1 << j
        hex_result.append(hex_digits[decimal_value])

    return "".join(hex_result)

if __name__ == '__main__':
    sample_binary_values = [
        "0",
        "1",
        "1010",
        "1111",
        "10101010",
        "11110000",
        "11011111",
        "00001111",
        "10000000",
        "11111111"
    ]

    for binary_val in sample_binary_values:
        hex_result = binary_to_hex(binary_val)
        print(f"{binary_val} -> {hex_result}")