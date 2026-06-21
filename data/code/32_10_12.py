def binary_to_hex(binary_string):
    if not binary_string:
        return "0"
    binary_string = binary_string.lstrip('0')
    if not binary_string:
        return "0"
    length = len(binary_string)
    padding = (4 - length % 4) % 4
    binary_string = '0' * padding + binary_string
    hex_digits = "0123456789ABCDEF"
    result = []
    i = 0
    while i < len(binary_string):
        chunk = binary_string[i:i+4]
        value = 0
        for bit in chunk:
            value = (value << 1) | (1 if bit == '1' else 0)
        result.append(hex_digits[value])
        i += 4
    return "".join(result)

if __name__ == '__main__':
    samples = ["1010", "0000", "11111111", "00010101", "1000000000000000"]
    for s in samples:
        print(binary_to_hex(s))