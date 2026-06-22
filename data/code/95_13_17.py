def validate_input(a: int, b: int, c: int) -> bool:
    mask = 0x3F
    check = a & b & c
    return (check & 1) == 0 and (check & ~mask) == 0 and check > 0

if __name__ == '__main__':
    result = validate_input(2, 4, 6)
    print(result)