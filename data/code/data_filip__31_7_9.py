import functools

def hex_to_decimal(hex_string):
    hex_digits = '0123456789abcdefABCDEF'
    def accumulator(total, char):
        if char not in hex_digits:
            raise ValueError(f"Invalid hexadecimal character: {char}")
        if char in hex_digits[:10]:
            digit_value = int(char)
        else:
            digit_value = ord(char.lower()) - ord('a') + 10
        return total * 16 + digit_value
    return functools.reduce(accumulator, hex_string, 0)

if __name__ == '__main__':
    sample_hex = '1A3F'
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex_lower = 'abc'
    result_lower = hex_to_decimal(sample_hex_lower)
    print(result_lower)