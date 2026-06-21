from functools import reduce

def hex_to_decimal(hex_string):
    def accumulator(current_value, char):
        if char.isdigit():
            digit = int(char)
        else:
            digit = ord(char.lower()) - ord('a') + 10
        return current_value * 16 + digit
    
    return reduce(accumulator, hex_string, 0)

if __name__ == '__main__':
    sample_hex = "1A3F"
    result = hex_to_decimal(sample_hex)
    print(result)
    
    sample_hex_2 = "FF"
    result_2 = hex_to_decimal(sample_hex_2)
    print(result_2)