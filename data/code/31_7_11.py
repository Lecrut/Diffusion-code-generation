from functools import reduce

def hex_to_decimal(hex_string):
    def char_to_int(char):
        if '0' <= char <= '9':
            return ord(char) - ord('0')
        elif 'a' <= char <= 'f':
            return ord(char) - ord('a') + 10
        elif 'A' <= char <= 'F':
            return ord(char) - ord('A') + 10
        else:
            raise ValueError(f"Invalid hexadecimal character: {char}")
    
    hex_string = hex_string.lower()
    return reduce(lambda acc, x: acc * 16 + x, map(char_to_int, hex_string), 0)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)