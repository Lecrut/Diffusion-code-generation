def hex_to_decimal(hex_string):
    if not hex_string:
        raise ValueError("Empty input")
    cleaned = hex_string.lstrip('0x')
    if not cleaned:
        raise ValueError("Invalid hex string")
    value = 0
    for char in cleaned:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError("Invalid hex character: {}".format(char))
        value = value * 16 + digit
    return value

if __name__ == '__main__':
    test_cases = [
        ("0", 0),
        ("1", 1),
        ("A", 10),
        ("F", 15),
        ("f", 15),
        ("10", 16),
        ("FF", 255),
        ("ff", 255),
        ("1A3", 419),
        ("0x1A3", 419),
        ("0X1a3", 419),
        ("DeadBeef", 3735928559),
        ("DEADBEEF", 3735928559),
    ]
    for hex_val, expected in test_cases:
        result = hex_to_decimal(hex_val)
        print("{} -> {} (expected {})".format(hex_val, result, expected))