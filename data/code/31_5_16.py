def hex_to_dec(hex_code: str) -> int:
    return int(hex_code, 16)

if __name__ == '__main__':
    print(hex_to_dec("ff"))