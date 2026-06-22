def hex_to_dec(hex_string):
    hex_digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    result = 0
    for char in hex_string:
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = result * 16 + hex_digits[char]
    return result

if __name__ == '__main__':
    sample_input = "1A3F"
    print(hex_to_dec(sample_input))