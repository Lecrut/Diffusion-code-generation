VALIDATION_RULES = {"positive": lambda n: n > 0, "less_than_100": lambda n: n < 100, "even": lambda n: (n & 1) == 0}

def validate_input(a: int, b: int, c: int) -> bool:
    checks = list(VALIDATION_RULES.values())
    for val in (a, b, c):
        for check in checks:
            if not check(val):
                return False
    return True

if __name__ == '__main__':
    a, b, c = 4, 8, 12
    print(validate_input(a, b, c))