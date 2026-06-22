def hex_to_int(hex_string: str) -> int:
    negative = False
    start_index = 0
    if hex_string.startswith('-'):
        negative = True
        start_index = 1
    elif hex_string.startswith('+'):
        start_index = 1

    value = 0
    digit_map = {}
    for i, char in enumerate('0123456789abcdefABCDEF'):
        digit_map[char] = i if i < 10 else i - 6 if char.islower() else i - 7 if char.isupper() and char in 'ABCDEF' else 0
        if char in '0123456789':
            digit_map[char] = int(char)
        elif char in 'abcdef':
            digit_map[char] = 10 + (ord(char) - ord('a'))
        elif char in 'ABCDEF':
            digit_map[char] = 10 + (ord(char) - ord('A'))

    for char in hex_string[start_index:]:
        value = value * 16 + digit_map[char]

    return -value if negative else value

if __name__ == '__main__':
    sample_hex = "1a3f"
    result = hex_to_int(sample_hex)
    print(result)
    negative_sample = "-FF"
    negative_result = hex_to_int(negative_sample)
    print(negative_result)