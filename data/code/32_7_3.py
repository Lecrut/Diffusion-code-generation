def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    padding = (4 - len(binary_str) % 4) % 4
    padded = '0' * padding + binary_str
    nibbles = [padded[i:i+4] for i in range(0, len(padded), 4)]
    hex_digits = []
    for nibble in nibbles:
        val = sum(int(b) * (2 ** (3 - idx)) for idx, b in enumerate(nibble))
        hex_digits.append(format(val, 'x'))
    return ''.join(hex_digits).lstrip('0') or '0'

if __name__ == '__main__':
    binary_value = '101010101010'
    result = binary_to_hex(binary_value)
    print(result)