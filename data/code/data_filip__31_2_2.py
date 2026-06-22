def hex_to_dec(hex_str):
    hex_str = hex_str.strip()
    if not hex_str:
        raise ValueError("Empty string provided")
    is_negative = False
    if hex_str.startswith('-'):
        is_negative = True
        hex_str = hex_str[1:]
    if not hex_str:
        raise ValueError("Empty string after sign removal")
    value_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    result = 0
    for char in hex_str:
        if char not in value_map:
            raise ValueError(f"Invalid hex character: {char}")
        digit_val = value_map[char]
        result = result * 16 + digit_val
    if is_negative:
        return -result
    return result

if __name__ == '__main__':
    test_cases = [
        ("0", 0),
        ("A", 10),
        ("FF", 255),
        ("ff", 255),
        ("10", 16),
        ("100", 256),
        ("DEAD", 57005),
        ("-10", -16),
        ("-FF", -255),
        ("aBcD", 43981)
    ]
    for hex_val, expected in test_cases:
        result = hex_to_dec(hex_val)
        print(f"hex_to_dec('{hex_val}') = {result}, expected = {expected}")
        if result != expected:
            print("MISMATCH")
        else:
            print("MATCH")