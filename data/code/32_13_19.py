def binary_to_hex(binary_string: str) -> str:
    hex_digits = '0123456789ABCDEF'
    padded_binary = binary_string.zfill(((len(binary_string) + 3) // 4) * 4)
    hex_result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i+4]
        value = int(chunk, 2)
        hex_result.append(hex_digits[value])
    return ''.join(hex_result)

if __name__ == '__main__':
    sample_binary = '1010111100001111'
    print(binary_to_hex(sample_binary))