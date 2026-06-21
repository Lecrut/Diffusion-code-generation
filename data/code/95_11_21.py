def validate_three_values(val_a, val_b, val_c):
    threshold = 100
    is_positive = lambda n: n > 0
    is_even = lambda n: n % 2 == 0
    is_under_limit = lambda n: n < threshold

    conditions = [is_positive, is_even, is_under_limit]
    values = [val_a, val_b, val_c]

    for condition in conditions:
        for value in values:
            if not condition(value):
                return False
    return True

if __name__ == '__main__':
    print(validate_three_values(12, 24, 36))
    print(validate_three_values(12, 25, 36))
    print(validate_three_values(102, 24, 36))
    print(validate_three_values(-12, 24, 36))