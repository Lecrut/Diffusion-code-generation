def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    samples = [
        ([True, False, False], "mixed_with_true"),
        ([False, False, False], "all_false"),
        ([], "empty"),
        ([True, True, True], "all_true"),
        ([False], "single_false"),
    ]
    for data, name in samples:
        print(f"{name}: {check_any_true(data)}")