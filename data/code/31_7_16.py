from functools import reduce

def hex_to_decimal(hex_string):
    hex_string = hex_string.upper()
    def accumulate(value, char):
        return value * 16 + int(char, 16)
    return reduce(accumulate, hex_string, 0)

if __name__ == '__main__':
    sample_values = ['0', '1a', 'FF', '1a2b3c']
    for sample in sample_values:
        result = hex_to_decimal(sample)
        print(f'{sample} -> {result}')