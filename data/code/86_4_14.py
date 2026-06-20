def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it, None)
    for curr in it:
        if (prev, curr) == (True, True):
            yield True
        else:
            yield False
        prev = curr

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(compare_pairs(sample_values)))