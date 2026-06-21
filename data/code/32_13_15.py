def bin_to_hex(binary_str):
    hex_digits = '0123456789abcdef'
    result = []
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    for i in range(0, len(padded), 4):
        chunk = padded[i:i + 4]
        decimal_value = int(chunk, 2)
        result.append(hex_digits[decimal_value])
    return ''.join(result)

if __name__ == '__main__':
    sample_binary = "110101101011"
    hex_result = bin_to_hex(sample_binary)
    print(hex_result)