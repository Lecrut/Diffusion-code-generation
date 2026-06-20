def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it, None)
    if prev is None:
        raise ValueError("Input iterable must not be empty")
    for curr in it:
        yield (prev, curr) == (True, True)
        prev = curr

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(compare_pairs(sample_values)))