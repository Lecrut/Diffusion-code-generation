def hex_to_dec(hex_string):
    hex_chars = "0123456789abcdefABCDEF"
    if not hex_string:
        return 0
    
    negative = False
    start_index = 0
    
    if hex_string[0] == '-':
        negative = True
        start_index = 1
    elif hex_string[0] == '+':
        start_index = 1
    
    if start_index >= len(hex_string):
        return 0
        
    for i in range(start_index, len(hex_string)):
        if hex_string[i] not in hex_chars:
            raise ValueError(f"Invalid character in hex string: {hex_string[i]}")
            
    decimal_value = 0
    power = 0
    
    for i in range(len(hex_string) - 1, start_index - 1, -1):
        char = hex_string[i]
        if char in "0123456789":
            digit_value = ord(char) - ord('0')
        elif char in "abcdef":
            digit_value = ord(char) - ord('a') + 10
        elif char in "ABCDEF":
            digit_value = ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid character: {char}")
            
        decimal_value += digit_value * (16 ** power)
        power += 1
        
    if negative:
        return -decimal_value
        
    return decimal_value

if __name__ == '__main__':
    test_cases = [
        "1A",
        "ff",
        "0",
        "FFF",
        "-10",
        "+2B",
        "a"
    ]
    
    for tc in test_cases:
        result = hex_to_dec(tc)
        print(f"hex_to_dec('{tc}') = {result}")