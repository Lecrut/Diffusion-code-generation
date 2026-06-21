def validate_triplet(a, b, c):
    criteria = {
        "positive": lambda x: x > 0,
        "even": lambda x: x % 2 == 0,
        "under_100": lambda x: x < 100
    }
    values = (a, b, c)
    for check in criteria.values():
        if not all(check(v) for v in values):
            return False
    return True

if __name__ == '__main__':
    print(validate_triplet(10, 20, 30))
    print(validate_triplet(10, 21, 30))
    print(validate_triplet(10, 20, 100))
    print(validate_triplet(-10, 20, 30))