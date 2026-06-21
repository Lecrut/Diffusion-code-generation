def hex_to_dec(hex_string):
    hex_string = hex_string.strip()
    if not hex_string:
        raise ValueError("Empty hex string")
    
    negative = False
    if hex_string.startswith('-'):
        negative = True
        hex_string = hex_string[1:]
    elif hex_string.startswith('+'):
        hex_string = hex_string[1:]
    
    if not hex_string:
        raise ValueError("Invalid hex string")
    
    valid_chars = "0123456789abcdefABCDEF"
    for char in hex_string:
        if char not in valid_chars:
            raise ValueError(f"Invalid character in hex string: {char}")
    
    value = 0
    multiplier = 1
    
    for i in range(len(hex_string) - 1, -1, -1):
        char = hex_string[i]
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            digit = ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            digit = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid character: {char}")
        
        value += digit * multiplier
        multiplier *= 16
    
    return -value if negative else value

if __name__ == '__main__':
    test_cases = ["FF", "ff", "10", "A1b2", "-FF", "+10", "0"]
    results = []
    for tc in test_cases:
        results.append(hex_to_dec(tc))
    
    print(results)