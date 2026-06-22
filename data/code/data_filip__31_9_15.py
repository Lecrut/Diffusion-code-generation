def hex_to_int(hex_string):
    hex_string = hex_string.strip()
    if hex_string.startswith(('0x', '0X')):
        hex_string = hex_string[2:]
    if not hex_string:
        raise ValueError("Empty hex string")
    value = 0
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    if not hex_string:
        raise ValueError("Invalid hex string")
    for char in hex_string:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hex character: {char}")
        value = value * 16 + digit
    return -value if negative else value

if __name__ == '__main__':
    test_cases = ["1A", "FF", "0x1A", "abc", "-ff"]
    for tc in test_cases:
        print(hex_to_int(tc))