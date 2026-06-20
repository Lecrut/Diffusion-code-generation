def compare_pairs(iterable):
    it = iter(iterable)
    try:
        prev = next(it)
        for curr in it:
            yield (prev, curr) == (True, True)
            prev = curr
    except StopIteration:
        return

if __name__ == '__main__':
    sample_values = [False, True, False, True, False]
    print(list(compare_pairs(sample_values)))