def binary_to_hex(binary_str):
    if not binary_str:
        return '0'
    clean = binary_str.lstrip('0')
    if not clean:
        return '0'
    val = int(clean, 2)
    hex_digits = []
    while val > 0:
        rem = val % 16
        if rem < 10:
            hex_digits.append(chr(ord('0') + rem))
        else:
            hex_digits.append(chr(ord('A') + rem - 10))
        val //= 16
    return ''.join(reversed(hex_digits))

if __name__ == '__main__':
    samples = ['0000', '1010', '11110000', '1', '0001010']
    for s in samples:
        print(binary_to_hex(s))