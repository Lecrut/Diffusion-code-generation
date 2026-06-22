def hex_to_decimal(hex_string: str) -> int:
    hex_string = hex_string.strip().lower()
    if hex_string.startswith(('0x', '-0x', '+0x')):
        if hex_string[0] == '-':
            sign = -1
            prefix_len = 3
        elif hex_string[0] == '+':
            sign = 1
            prefix_len = 2
        else:
            sign = 1
            prefix_len = 2
        hex_digits = hex_string[prefix_len:]
    else:
        sign = 1
        hex_digits = hex_string

    if not hex_digits:
        return 0

    decimal_value = 0
    for char in hex_digits:
        decimal_value *= 16
        if '0' <= char <= '9':
            decimal_value += ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            decimal_value += ord(char) - ord('a') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")

    return sign * decimal_value

if __name__ == '__main__':
    hex_strings = ['1a3f', '0x10', '-ff', '0', '100']
    for h in hex_strings:
        result = hex_to_decimal(h)
        print(result)