def check_both_false(a: bool, b: bool) -> bool:
    return not a and not b

if __name__ == '__main__':
    sample_values = {
        'both_false': (False, False),
        'first_true': (True, False),
        'second_true': (False, True),
        'both_true': (True, True)
    }

    for label, (a, b) in sample_values.items():
        result = check_both_false(a, b)
        print(f'{label}: {result}')