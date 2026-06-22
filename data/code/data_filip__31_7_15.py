from functools import reduce

def hex_to_decimal(hex_string):
    def accumulator(value, char):
        digit_value = int(char, 16)
        return value * 16 + digit_value

    return reduce(accumulator, hex_string.upper(), 0)

if __name__ == '__main__':
    sample_hex = '1A3F'
    result = hex_to_decimal(sample_hex)
    print(result)
    sample_hex2 = 'FF'
    result2 = hex_to_decimal(sample_hex2)
    print(result2)
    sample_hex3 = '0'
    result3 = hex_to_decimal(sample_hex3)
    print(result3)