def hex_to_decimal(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError("Empty hex string")
    
    negative = False
    if hex_string[0] == '-':
        negative = True
        hex_string = hex_string[1:]
    elif hex_string[0] == '+':
        hex_string = hex_string[1:]
    
    if not hex_string:
        raise ValueError("Invalid hex string")
    
    valid_chars = set('0123456789abcdefABCDEF')
    if not all(c in valid_chars for c in hex_string):
        raise ValueError("Invalid character in hex string")
    
    value_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    
    result = 0
    power = 1
    for i in range(len(hex_string) - 1, -1, -1):
        digit = hex_string[i]
        result += value_map[digit] * power
        power *= 16
    
    if negative:
        result = -result
    
    return result

if __name__ == '__main__':
    test_cases = [
        "0", "1", "F", "f", "10", "FF", "ff", "100", "ABC", "abc", "-F", "-FF"
    ]
    for case in test_cases:
        print(hex_to_decimal(case))