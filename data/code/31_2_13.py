def hex_to_dec(hex_code):
    hex_code = hex_code.strip()
    if hex_code.startswith(('0x', '0X')):
        hex_code = hex_code[2:]
    
    is_negative = False
    if hex_code.startswith('-'):
        is_negative = True
        hex_code = hex_code[1:]
    
    valid_chars = set('0123456789abcdefABCDEF')
    for char in hex_code:
        if char not in valid_chars:
            raise ValueError(f"Invalid hexadecimal digit: {char}")
    
    decimal_value = 0
    power = 0
    for char in reversed(hex_code):
        if char.isdigit():
            digit = ord(char) - ord('0')
        elif 'a' <= char.lower() <= 'f':
            digit = ord(char.lower()) - ord('a') + 10
        decimal_value += digit * (16 ** power)
        power += 1
    
    if is_negative:
        decimal_value = -decimal_value
    
    return decimal_value

if __name__ == '__main__':
    test_cases = [
        ("FF", 255),
        ("ff", 255),
        ("1a3", 419),
        ("1A3", 419),
        ("0x1F", 31),
        ("0X1F", 31),
        ("0", 0),
        ("00", 0),
        ("-FF", -255),
        ("0x0", 0)
    ]
    
    results = []
    for hex_code, expected in test_cases:
        result = hex_to_dec(hex_code)
        results.append((hex_code, result, expected, result == expected))
    
    for hex_code, result, expected, is_correct in results:
        if not is_correct:
            print(f"FAIL: {hex_code} -> {result} (expected {expected})")
        else:
            print(f"OK: {hex_code} -> {result}")