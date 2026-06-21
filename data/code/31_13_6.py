def hex_to_decimal(hex_string: str) -> int:
    result: int = 0
    multiplier: int = 1
    for char in hex_string[::-1]:
        if char.isalpha():
            value: int = ord(char.upper()) - ord('A') + 10
        else:
            value: int = ord(char) - ord('0')
        result += value * multiplier
        multiplier *= 16
    return result

if __name__ == '__main__':
    print(hex_to_decimal("1A3F"))