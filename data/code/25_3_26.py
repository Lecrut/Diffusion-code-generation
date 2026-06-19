def contains_zero(iterable):
    for number in iterable:
        if number == 0:
            yield True
    yield False
if __name__ == '__main__':
    sample_values = [1, 2, 3, 0, 4, 5]
    generator = contains_zero(sample_values)
    result = next(generator)
    print(result)