def hex_to_decimal(hex_string: str) -> int:
    return int(hex_string, 16)

if __name__ == '__main__':
    result = hex_to_decimal("1A3F")
    print(result)