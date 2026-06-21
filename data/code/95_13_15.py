MAX_LIMIT = 100
MIN_LIMIT = 0

def validate_input(a: int, b: int, c: int) -> bool:
    mask = 1
    check = lambda n: n > MIN_LIMIT and n < MAX_LIMIT and (n & mask) == 0
    return check(a) and check(b) and check(c)

if __name__ == '__main__':
    val1 = validate_input(2, 4, 6)
    print(val1)
    val2 = validate_input(2, 4, 5)
    print(val2)
    val3 = validate_input(0, 4, 6)
    print(val3)
    val4 = validate_input(2, 4, 100)
    print(val4)
    val5 = validate_input(-2, 4, 6)
    print(val5)