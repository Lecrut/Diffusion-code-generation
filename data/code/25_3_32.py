def contains_zero(iterable):
    for number in iterable:
        if number == 0:
            yield True
            return
    yield False

if __name__ == '__main__':
    sample_values = [1, 2, 3, 0, 4, 5]
    result_generator = contains_zero(sample_values)
    print(next(result_generator))