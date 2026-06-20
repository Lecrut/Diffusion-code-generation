def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    sample_values = [False, False, True, False]
    print(any_true(sample_values))