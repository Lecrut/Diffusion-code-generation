def hex_to_decimal(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError('Input must be a string')
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError('Input string cannot be empty')
    try:
        return int(hex_string, 16)
    except ValueError:
        raise ValueError(f'Invalid hexadecimal string: {hex_string}')

def hex_to_decimal_memory_efficient(hex_string: str) -> int:
    if not isinstance(hex_string, str):
        raise TypeError('Input must be a string')
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError('Input string cannot be empty')
    index = 0
    negative = False
    if hex_string[index] == '-':
        negative = True
        index += 1
    elif hex_string[index] == '+':
        index += 1
    if index + 1 < len(hex_string) and hex_string[index] == '0' and (hex_string[index + 1].lower() == 'x'):
        index += 2
    result = 0
    hex_digits = '0123456789abcdef'
    for char in hex_string[index:]:
        char_lower = char.lower()
        if char_lower not in hex_digits:
            raise ValueError(f'Invalid hexadecimal character: {char}')
        digit_value = hex_digits.index(char_lower)
        result = result * 16 + digit_value
    return -result if negative else result
if __name__ == '__main__':
    sample_hex_values = ['1A', 'FF', '0x10', '0XFF', '-2A', '+3B', '0', '100', 'F00D', 'deadbeef']
    for hex_val in sample_hex_values:
        try:
            decimal_val = hex_to_decimal(hex_val)
            print(f"hex_to_decimal('{hex_val}') = {decimal_val}")
        except ValueError as e:
            print(f"hex_to_decimal('{hex_val}') raised ValueError: {e}")
    print()
    for hex_val in sample_hex_values:
        try:
            decimal_val = hex_to_decimal_memory_efficient(hex_val)
            print(f"hex_to_decimal_memory_efficient('{hex_val}') = {decimal_val}")
        except ValueError as e:
            print(f"hex_to_decimal_memory_efficient('{hex_val}') raised ValueError: {e}")