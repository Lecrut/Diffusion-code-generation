def hex_to_dec(hex_str: str) -> int:
    hex_digits = '0123456789ABCDEF'
    hex_digits_lower = '0123456789abcdef'
    result = 0
    multiplier = 1
    for char in reversed(hex_str):
        if char in hex_digits:
            value = hex_digits.index(char)
        elif char in hex_digits_lower:
            value = hex_digits_lower.index(char)
        else:
            raise ValueError(f"Invalid hex character: {char}")
        result += value * multiplier
        multiplier *= 16
    return result

if __name__ == '__main__':
    print(hex_to_dec('A1'))
    print(hex_to_dec('ff'))
    print(hex_to_dec('0'))
    print(hex_to_dec('10'))