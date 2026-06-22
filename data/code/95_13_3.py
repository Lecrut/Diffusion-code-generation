def validate_input(a: int, b: int, c: int) -> bool:
    def check(n: int) -> bool:
        return n > 0 and n < 100 and (n & 1) == 0
    return check(a) and check(b) and check(c)

if __name__ == '__main__':
    result = validate_input(2, 4, 6)
    print(result)