def hex_to_int(hex_string):
    if not isinstance(hex_string, str):
        raise ValueError("Input must be a string")
    if not hex_string:
        raise ValueError("Input string cannot be empty")
    
    if hex_string.startswith(("0x", "0X")):
        core = hex_string[2:]
    else:
        core = hex_string
    
    if not core:
        raise ValueError("No valid hex digits found")
    
    for char in core:
        if char not in "0123456789abcdefABCDEF":
            raise ValueError(f"Invalid character '{char}' in hex string")
    
    return int(core, 16)

if __name__ == '__main__':
    test_cases = ["0x1A", "FF", "0X100", "g1", "0x", ""]
    
    for case in test_cases:
        try:
            result = hex_to_int(case)
            print(result)
        except ValueError as e:
            print(f"ValueError: {e}")