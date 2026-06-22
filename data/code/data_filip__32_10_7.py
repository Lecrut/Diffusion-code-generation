def binary_to_hex(binary_string):
    if not binary_string or not all(c in '01' for c in binary_string):
        raise ValueError("Input must be a non-empty binary string containing only 0s and 1s")
    if len(binary_string) == 0:
        return '0'
    padded_length = (len(binary_string) + 3) // 4 * 4
    padded_binary = binary_string.zfill(padded_length)
    hex_chars = '0123456789ABCDEF'
    result = []
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) | int(bit)
        result.append(hex_chars[value])
    return ''.join(result).lstrip('0') or '0'

if __name__ == '__main__':
    test_cases = ['0', '1', '10', '1010', '11111111', '00001010', '1111000011110000']
    for binary in test_cases:
        print(f"{binary} -> {binary_to_hex(binary)}")
    print(binary_to_hex('101101100101'))