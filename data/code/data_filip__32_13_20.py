def binary_to_hex(binary_str):
    hex_digits = "0123456789abcdef"
    if len(binary_str) % 4 != 0:
        binary_str = binary_str.zfill((len(binary_str) + 4) // 4 * 4)
    hex_result = ""
    for i in range(0, len(binary_str), 4):
        nibble = binary_str[i:i+4]
        value = int(nibble, 2)
        hex_result += hex_digits[value]
    return hex_result

if __name__ == '__main__':
    binary_data = "1111100101101001"
    result = binary_to_hex(binary_data)
    print(result)