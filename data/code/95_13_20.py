VALIDATION_RULES = {
    "positive": lambda n: n > 0,
    "even": lambda n: (n & 1) == 0,
    "under_100": lambda n: n < 100
}

def validate_input(a: int, b: int, c: int) -> bool:
    values = [a, b, c]
    for n in values:
        for rule in VALIDATION_RULES.values():
            if not rule(n):
                return False
    return True

if __name__ == '__main__':
    result = validate_input(2, 4, 6)
    print(result)
    result2 = validate_input(2, 4, 100)
    print(result2)
    result3 = validate_input(-2, 4, 6)
    print(result3)
    result4 = validate_input(2, 3, 6)
    print(result4)