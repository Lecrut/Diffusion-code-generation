def contains_zero(iterable):
    ZEROTHRESHOLD = 0
    for number in iterable:
        if number == ZEROTHRESHOLD:
            yield True
            return
    yield False

if __name__ == '__main__':
    SAMPLE_VALUES = [7, 8, 9, 0, 10]
    result_generator = contains_zero(SAMPLE_VALUES)
    print(next(result_generator))