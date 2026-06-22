def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    chunks = [padded[i:i + 4] for i in range(0, len(padded), 4)]
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    result = ''.join([hex_digits[int(chunk, 2)] for chunk in chunks])
    return result

if __name__ == '__main__':
    sample_binaries = ['1010', '11110000', '101010101010', '1', '11111111']
    for b in sample_binaries:
        print(f"{b} -> {binary_to_hex(b)}")