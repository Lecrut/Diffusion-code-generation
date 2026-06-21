def binary_to_hex(binary_str: str) -> str:
    hex_digits = '0123456789ABCDEF'
    if not binary_str:
        return '0'
    padded_len = len(binary_str) + 3 & ~3
    padded_binary = binary_str.zfill(padded_len)
    hex_result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i + 4]
        decimal_value = 0
        for bit in chunk:
            decimal_value = (decimal_value << 1) + int(bit)
        hex_result.append(hex_digits[decimal_value])
    return ''.join(hex_result)
if __name__ == '__main__':
    sample_binary = '110101101010101011110000'
    result = binary_to_hex(sample_binary)
    print(result)