def binary_to_hex(binary_string: str) -> str:
    if not binary_string:
        return "0"
    
    binary_string = binary_string.lstrip("0")
    if not binary_string:
        return "0"
    
    length = len(binary_string)
    padding_needed = (4 - (length % 4)) % 4
    padded_binary = "0" * padding_needed + binary_string
    
    hex_chars = "0123456789ABCDEF"
    result = []
    
    for i in range(0, len(padded_binary), 4):
        chunk = padded_binary[i : i + 4]
        value = 0
        for char in chunk:
            value = (value << 1) | int(char)
        result.append(hex_chars[value])
    
    return "".join(result)

if __name__ == "__main__":
    sample_1 = "1010"
    sample_2 = "11110000"
    sample_3 = "00000101"
    sample_4 = ""
    sample_5 = "0000"
    
    print(binary_to_hex(sample_1))
    print(binary_to_hex(sample_2))
    print(binary_to_hex(sample_3))
    print(binary_to_hex(sample_4))
    print(binary_to_hex(sample_5))