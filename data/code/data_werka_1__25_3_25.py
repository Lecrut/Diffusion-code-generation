def contains_zero(iterable):
    for item in iterable:
        if item == 0:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_values = [1, 2, 3, 0, 5]
    result = next(contains_zero(sample_values))
    print(result)