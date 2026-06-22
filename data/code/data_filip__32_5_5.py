def binary_to_hex_chunked(binary_string, chunk_size=1024 * 1024):
    hex_chars = "0123456789abcdef"
    lookup = {f"{a}{b}{c}{d}": hex_chars[int(a, 2) << 3 | int(b, 2) << 2 | int(c, 2) << 1 | int(d, 2)]
              for a in "01" for b in "01" for c in "01" for d in "01"}
    remainder = len(binary_string) % 4
    if remainder:
        padded = binary_string[:remainder] + "0" * (4 - remainder) + binary_string[remainder:]
    else:
        padded = binary_string
    result = []
    for i in range(0, len(padded), chunk_size * 4):
        chunk = padded[i:i + chunk_size * 4]
        chunk_hex = []
        for j in range(0, len(chunk), 4):
            nibble = chunk[j:j + 4]
            chunk_hex.append(lookup[nibble])
        result.append("".join(chunk_hex))
    return "".join(result)

if __name__ == '__main__':
    sample_binary = "1010101111001101" * 1000
    hex_result = binary_to_hex_chunked(sample_binary)
    print(hex_result)