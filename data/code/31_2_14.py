def hex_to_dec(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError("Empty string provided")
    is_negative = False
    if hex_string.startswith('-'):
        is_negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    
    if not hex_string:
        raise ValueError("Empty string provided")
    
    digit_map = {}
    for i, char in enumerate("0123456789abcdefABCDEF"):
        val = i if i < 10 else i - 10
        digit_map[char] = val
    
    result = 0
    for char in hex_string:
        if char not in digit_map:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        result = result * 16 + digit_map[char]
    
    return -result if is_negative else result

if __name__ == '__main__':
    test_cases = [
        "0",
        "F",
        "f",
        "10",
        "FF",
        "ff",
        "1A3F",
        "-10",
        "-ff",
        "123456789ABCDEF"
    ]
    for case in test_cases:
        print(hex_to_dec(case))