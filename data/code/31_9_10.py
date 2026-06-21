def hex_string_to_integer(hex_str: str) -> int:
    hex_str = hex_str.strip().lower()
    if hex_str.startswith("0x"):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    result = 0
    for char in hex_str:
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit_value = ord(char) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = (result << 4) + digit_value
    return result

if __name__ == '__main__':
    sample_hex = "1a3f"
    sample_hex_prefixed = "0x1A3F"
    sample_negative = "-1f"
    
    print(hex_string_to_integer(sample_hex))
    print(hex_string_to_integer(sample_hex_prefixed))
    if sample_negative.startswith("-"):
        print(-hex_string_to_integer(sample_negative[1:]))
    else:
        print(hex_string_to_integer(sample_negative))