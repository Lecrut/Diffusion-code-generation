def compare_bool_pairs(iterable):
    it = iter(iterable)
    try:
        prev = next(it)
    except StopIteration:
        return
    for curr in it:
        yield prev == curr
        prev = curr

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(compare_bool_pairs(sample_values)))