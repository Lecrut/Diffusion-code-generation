def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_values = [
        [False, False, True, False],
        [False, False, False],
        [True],
        [],
        [False, False, False, False]
    ]
    for i, values in enumerate(sample_values):
        print(f"sample_{i+1}: {check_any_true(values)}")