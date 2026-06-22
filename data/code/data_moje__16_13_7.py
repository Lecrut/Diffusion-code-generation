def get_first_from_generator(generator):
    try:
        return next(generator)
    except StopIteration:
        return None

if __name__ == '__main__':
    def sample_gen():
        yield 1
        yield 2
        yield 3

    result = get_first_from_generator(sample_gen())
    print(result)