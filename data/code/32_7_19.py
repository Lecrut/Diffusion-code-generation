def binary_to_hex(binary_str):
    padded = binary_str.zfill((len(binary_str) + 3) // 4 * 4)
    groups = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex_vals = [hex_digits[int(group, 2)] for group in groups]
    return ''.join(hex_vals)

if __name__ == '__main__':
    print(binary_to_hex('1010'))
    print(binary_to_hex('11110000'))
    print(binary_to_hex('1'))