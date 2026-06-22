def hex_to_int(hex_code: str) -> int:
    return int(hex_code, 16)

if __name__ == '__main__':
    result = hex_to_int("FF")
    print(result)