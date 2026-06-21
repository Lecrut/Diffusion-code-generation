def binary_to_hex(binary_string):
    binary_string = binary_string.strip()
    if not binary_string:
        return ""

    padding_length = (4 - len(binary_string) % 4) % 4
    padded_binary = "0" * padding_length + binary_string

    hex_chars = "0123456789ABCDEF"
    result = []

    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i + 4]
        value = 0
        for bit in nibble:
            value = value * 2 + (1 if bit == '1' else 0)
        result.append(hex_chars[value])

    return "".join(result)

if __name__ == '__main__':
    samples = ["1010", "1111", "0", "1", "11010111", "0000"]
    for sample in samples:
        print(binary_to_hex(sample))