def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it)
    for current in it:
        yield prev == current
        prev = current

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(compare_pairs(sample_values)))