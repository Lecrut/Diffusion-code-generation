def binary_to_hex(binary_string):
    binary_string = binary_string.replace("0b", "").replace(" ", "")
    remainder = 64 - len(binary_string)
    if remainder > 0:
        binary_string = "0" * remainder + binary_string
    hex_chars = "0123456789ABCDEF"
    pairs = zip(binary_string[::4], binary_string[1::4], binary_string[2::4], binary_string[3::4])
    hex_digits = [hex_chars[int("".join(p), 2)] for p in pairs]
    return "".join(hex_digits)

if __name__ == "__main__":
    sample_binary = "110110101111"
    result = binary_to_hex(sample_binary)
    print(result)