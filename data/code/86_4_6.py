TRUE = True

def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it)
    for curr in it:
        yield (prev, curr) == (TRUE, TRUE)
        prev = curr

if __name__ == '__main__':
    sample_values = [True, False, True, True, False]
    print(list(compare_pairs(sample_values)))