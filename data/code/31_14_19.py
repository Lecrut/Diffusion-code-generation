def hex_to_decimal(hex_string):
    hex_string = hex_string.lstrip('-')
    if hex_string.startswith('0x') or hex_string.startswith('0X'):
        hex_string = hex_string[2:]
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    negative = False
    original = hex_string
    if original and original[0] == '-':
        negative = True
        original = original[1:]
    result = 0
    for char in original.lower():
        value = hex_digits[char]
        result = result * 16 + value
    if negative:
        result = -result
    return result

if __name__ == '__main__':
    print(hex_to_decimal('1a'))
    print(hex_to_decimal('FF'))
    print(hex_to_decimal('0x1A'))
    print(hex_to_decimal('-FF'))
    print(hex_to_decimal('0'))
    print(hex_to_decimal('2A3F'))