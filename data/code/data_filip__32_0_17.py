def binary_to_hex(binary_str):
    if not binary_str:
        return "0"

    hex_chars = "0123456789abcdef"
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    hex_digits = []

    for i in range(0, len(padded), 4):
        nibble = padded[i:i+4]
        value = 0
        for bit in nibble:
            value = value * 2 + int(bit)
        hex_digits.append(hex_chars[value])

    result = "".join(hex_digits).lstrip("0")
    return result if result else "0"

if __name__ == '__main__':
    sample_binary = "110101101011"
    hex_result = binary_to_hex(sample_binary)
    print(hex_result)