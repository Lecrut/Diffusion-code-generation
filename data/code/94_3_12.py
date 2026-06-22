def check_any_true(values):
    status_map = {True: "has_true", False: "no_true"}
    if not values:
        return status_map[False]
    for val in values:
        if val:
            return status_map[True]
    return status_map[False]

if __name__ == '__main__':
    sample_data = [False, False, True, False]
    outcome = check_any_true(sample_data)
    print(outcome)