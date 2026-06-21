from functools import reduce

def hex_to_decimal(hex_str):
    hex_chars = "0123456789abcdef"
    hex_str_lower = hex_str.lower()
    
    def accumulator(acc, char):
        if char not in hex_chars:
            raise ValueError(f"Invalid hex character: {char}")
        digit_value = hex_chars.index(char)
        return acc * 16 + digit_value
    
    return reduce(accumulator, hex_str_lower, 0)

if __name__ == '__main__':
    hex_string = "1a3f"
    result = hex_to_decimal(hex_string)
    print(result)