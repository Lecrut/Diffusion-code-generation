import functools

def hex_to_decimal(hex_string):
    hex_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    if not hex_string:
        return 0
    result = functools.reduce(lambda acc, char: acc * 16 + hex_map[char], hex_string, 0)
    return result

if __name__ == '__main__':
    sample_hex_1 = "1A3F"
    sample_hex_2 = "DEADBEEF"
    sample_hex_3 = "ff"
    print(hex_to_decimal(sample_hex_1))
    print(hex_to_decimal(sample_hex_2))
    print(hex_to_decimal(sample_hex_3))