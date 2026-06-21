def hex_to_decimal(hex_str):
    if not hex_str:
        return 0
    hex_str = hex_str.strip()
    is_negative = False
    if hex_str.startswith('-'):
        is_negative = True
        hex_str = hex_str[1:]
    elif hex_str.startswith('+'):
        hex_str = hex_str[1:]
    if not hex_str:
        return 0
    if hex_str.startswith('0x') or hex_str.startswith('0X'):
        hex_str = hex_str[2:]
    if not hex_str:
        return 0
    for char in hex_str:
        if not ((char >= '0' and char <= '9') or (char >= 'a' and char <= 'f') or (char >= 'A' and char <= 'F')):
            raise ValueError("Invalid hexadecimal character")
    result = 0
    for char in hex_str:
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        else:
            digit = ord(char) - ord('A') + 10
        result = result * 16 + digit
    if is_negative:
        return -result
    return result

if __name__ == '__main__':
    test_cases = ["0", "1A", "FF", "ff", "10", "ABC", "0x1A", "-FF", "+10"]
    for case in test_cases:
        print(hex_to_decimal(case))