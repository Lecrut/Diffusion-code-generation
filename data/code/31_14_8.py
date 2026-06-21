def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        return 0
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    if not hex_string:
        return 0
    result = 0
    power = 0
    for i in range(len(hex_string) - 1, -1, -1):
        char = hex_string[i]
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit_value = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result += digit_value * (16 ** power)
        power += 1
    if is_negative:
        result = -result
    return result

if __name__ == '__main__':
    sample_hex = "1A3F"
    print(hex_to_decimal(sample_hex))
    sample_negative_hex = "-FF"
    print(hex_to_decimal(sample_negative_hex))
    sample_mixed_case = "0xdeadBEEF"
    print(hex_to_decimal(sample_mixed_case))