def hex_to_decimal(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string is empty")
    cleaned = hex_string
    if cleaned.startswith('0x') or cleaned.startswith('0X'):
        cleaned = cleaned[2:]
    if not cleaned:
        raise ValueError("Invalid hex string")
    valid_chars = set('0123456789abcdefABCDEF')
    for char in cleaned:
        if char not in valid_chars:
            raise ValueError("Invalid hex character: {}".format(char))
    return int(cleaned, 16)

if __name__ == '__main__':
    print(hex_to_decimal('1A'))
    print(hex_to_decimal('0xFF'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('deadBEEF'))
    try:
        hex_to_decimal('GG')
    except ValueError as e:
        print(e)
    try:
        hex_to_decimal('12G')
    except ValueError as e:
        print(e)
    try:
        hex_to_decimal('')
    except ValueError as e:
        print(e)
    try:
        hex_to_decimal(123)
    except ValueError as e:
        print(e)