def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if len(hex_string) == 0:
        raise ValueError("Hex string cannot be empty")
    allowed_chars = set('0123456789abcdefABCDEF')
    if not all(c in allowed_chars for c in hex_string):
        raise ValueError("Invalid hex character in string")
    return int(hex_string, 16)

if __name__ == '__main__':
    print(hex_to_decimal('1A'))
    print(hex_to_decimal('ff'))
    print(hex_to_decimal('0'))
    try:
        hex_to_decimal('G1')
    except ValueError:
        print('ValueError raised for G1')
    try:
        hex_to_decimal('')
    except ValueError:
        print('ValueError raised for empty string')
    try:
        hex_to_decimal('12 34')
    except ValueError:
        print('ValueError raised for space')