import functools

def hex_to_decimal(hex_str: str) -> int:
    digits = '0123456789abcdef'
    hex_str_lower = hex_str.lower()
    char_values = [digits.index(c) for c in hex_str_lower]
    
    def accumulator(acc, val):
        return acc * 16 + val
    
    result = functools.reduce(accumulator, char_values, 0)
    return result

if __name__ == '__main__':
    sample_hex = "1a3f"
    result = hex_to_decimal(sample_hex)
    print(result)