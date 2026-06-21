def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"

    padding_length = (4 - len(binary_string) % 4) % 4
    padded_binary = "0" * padding_length + binary_string

    hex_digits = "0123456789ABCDEF"
    result = []

    for i in range(0, len(padded_binary), 4):
        nibble = padded_binary[i:i + 4]
        decimal_value = 0
        for j, bit in enumerate(nibble):
            if bit == '1':
                decimal_value += 2 ** (3 - j)
        result.append(hex_digits[decimal_value])

    return "".join(result).lstrip("0") or "0"

if __name__ == '__main__':
    print(binary_to_hex("1010"))
    print(binary_to_hex("11110000"))
    print(binary_to_hex("11011110"))
    print(binary_to_hex("0"))
    print(binary_to_hex("1"))
    print(binary_to_hex("101010101010"))