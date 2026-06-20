def combine_checks(is_positive, is_even, is_less_than_100):
    conditions = {
        'positive': is_positive,
        'even': is_even,
        'less_than_100': is_less_than_100
    }
    summary = []
    for key, value in conditions.items():
        if value:
            summary.append(f"{key.capitalize()}")
    return ", ".join(summary) or "None"

if __name__ == '__main__':
    test_cases = [
        (True, True, True),
        (False, False, False),
        (True, False, False),
        (False, True, True),
        (True, True, False)
    ]
    for case in test_cases:
        print(f"Input: {case}")
        result = combine_checks(*case)
        print(f"Output: {result}\n")