def validate_values(a, b, c):
    conditions = [
        lambda x: x > 0,
        lambda x: x % 2 == 0,
        lambda x: x < 100
    ]
    for val in (a, b, c):
        for condition in conditions:
            if not condition(val):
                return False
    return True

if __name__ == '__main__':
    print(validate_values(10, 20, 30))
    print(validate_values(10, 21, 30))
    print(validate_values(10, 20, 100))
    print(validate_values(-10, 20, 30))