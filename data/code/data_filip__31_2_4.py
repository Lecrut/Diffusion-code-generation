def hex_to_dec(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]

    if not hex_string:
        raise ValueError("No valid hex digits found")

    digit_map = {}
    for i in range(10):
        digit_map[str(i)] = i
    for i in range(6):
        digit_map[chr(ord('a') + i)] = 10 + i
        digit_map[chr(ord('A') + i)] = 10 + i

    result = 0
    power = 0
    for char in reversed(hex_string):
        if char not in digit_map:
            raise ValueError(f"Invalid hex character: {char}")
        value = digit_map[char]
        result += value * (16 ** power)
        power += 1

    return -result if is_negative else result

if __name__ == '__main__':
    test_cases = [
        ("0", 0),
        ("10", 16),
        ("FF", 255),
        ("ff", 255),
        ("1A3", 419),
        ("abcdef", 11259375),
        ("-FF", -255),
        ("7B", 123)
    ]
    for hex_val, expected in test_cases:
        result = hex_to_dec(hex_val)
        print(f"hex_to_dec('{hex_val}') = {result}")
        if result != expected:
            print(f"Mismatch: expected {expected}, got {result}")