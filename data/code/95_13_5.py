def validate_input(a: int, b: int, c: int) -> bool:
    return (a > 0) and (b > 0) and (c > 0) and \
           (a < 100) and (b < 100) and (c < 100) and \
           ((a & 1) == 0) and ((b & 1) == 0) and ((c & 1) == 0)

if __name__ == '__main__':
    result = validate_input(2, 4, 6)
    print(result)
    result2 = validate_input(2, 3, 6)
    print(result2)
    result3 = validate_input(0, 4, 6)
    print(result3)
    result4 = validate_input(2, 4, 100)
    print(result4)