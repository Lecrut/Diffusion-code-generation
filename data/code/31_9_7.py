def hex_string_to_int(hex_str):
    result = 0
    power = 0
    i = len(hex_str) - 1
    while i >= 0:
        char = hex_str[i]
        if '0' <= char <= '9':
            digit = ord(char) - 48
        elif 'a' <= char <= 'f':
            digit = ord(char) - 87
        elif 'A' <= char <= 'F':
            digit = ord(char) - 55
        else:
            raise ValueError("Invalid hex character")
        result += digit * (16 ** power)
        power += 1
        i -= 1
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_string_to_int(sample_hex))
    sample_hex_2 = "FF"
    print(hex_string_to_int(sample_hex_2))