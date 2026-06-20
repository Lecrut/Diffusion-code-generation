def any_true(iterable):
    if not isinstance(iterable, (list, tuple, set)):
        raise ValueError("Input must be an iterable")
    return any(iterable)

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    print(any_true(sample_values))