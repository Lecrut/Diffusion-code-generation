def check_any_true(values):
    return any(values)

if __name__ == '__main__':
    sample_input = [False, True, False, False]
    outcome = check_any_true(sample_input)
    print(outcome)