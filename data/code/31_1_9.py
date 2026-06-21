def hex_to_decimal(hex_string: str) -> int:
    hex_string = hex_string.upper()
    decimal_value = 0
    length = len(hex_string)
    for i in range(length):
        char = hex_string[i]
        position = length - 1 - i
        if '0' <= char <= '9':
            digit_value = ord(char) - ord('0')
        elif 'A' <= char <= 'F':
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f'Invalid hexadecimal character: {char}')
        decimal_value += digit_value * 16 ** position
    return decimal_value
if __name__ == '__main__':
    hex_values = ['1A', 'FF', '0', '10', '100', 'ABCD']
    for hex_val in hex_values:
        result = hex_to_decimal(hex_val)
        print(result)