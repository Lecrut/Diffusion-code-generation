def binary_to_hex(binary_str):
    hex_digits = "0123456789abcdef"
    if not binary_str:
        return ""
    if len(binary_str) % 4 != 0:
        binary_str = binary_str.zfill(len(binary_str) + (4 - len(binary_str) % 4))
    result = []
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        decimal_value = 0
        for bit in nibble:
            decimal_value = (decimal_value << 1) + int(bit)
        result.append(hex_digits[decimal_value])
    return "".join(result)

if __name__ == '__main__':
    binary_data = "1111010110101010"
    print(binary_to_hex(binary_data))