def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it, None)
    for curr in it:
        yield (prev, curr) == (True, True)
        prev = curr

if __name__ == '__main__':
    sample_values = [False, True, True, False, True]
    result = list(compare_pairs(sample_values))
    print(result)