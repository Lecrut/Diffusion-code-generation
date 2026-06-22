def binary_to_hex(binary_string):
    padded_binary = binary_string if len(binary_string) % 4 == 0 else binary_string.zfill(((len(binary_string) + 3) // 4) * 4)
    chunks = [padded_binary[i:i+4] for i in range(0, len(padded_binary), 4)]
    hex_digits = [str(x) for x in range(10)] + [chr(ord('A') + i) for i in range(6)]
    mapping = {b: h for b, h in zip(['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'], hex_digits)}
    hex_parts = [mapping.get(chunk, '0') for chunk in chunks]
    return ''.join(hex_parts).lstrip('0') or '0'

if __name__ == '__main__':
    sample_binary = '1101011110101'
    result = binary_to_hex(sample_binary)
    print(result)