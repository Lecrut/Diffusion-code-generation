TRUE = True
FALSE = False

def compare_pairs(iterable):
    it = iter(iterable)
    prev = next(it, FALSE)
    for curr in it:
        yield (prev, curr) == (TRUE, TRUE)
        prev = curr

if __name__ == '__main__':
    sample_values = [TRUE, FALSE, TRUE, TRUE, FALSE]
    print(list(compare_pairs(sample_values)))