def hex_to_decimal(hex_str: str) -> int:
    return int(hex_str, 16)

if __name__ == '__main__':
    result = hex_to_decimal('1A3F')
    print(result)