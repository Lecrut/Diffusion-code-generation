def hex_to_int(hex_string):
    value = 0
    power = 1
    hex_digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for char in reversed(hex_string):
        if char in hex_digits:
            value += hex_digits[char] * power
            power *= 16
        else:
            raise ValueError(f"Invalid hex character: {char}")
    return value

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_int(sample_hex)
    print(result)