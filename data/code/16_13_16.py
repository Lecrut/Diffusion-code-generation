def get_first_element(generator):
    return next(generator)

if __name__ == '__main__':
    def sample_gen():
        yield 1
        yield 2
        yield 3

    result = get_first_element(sample_gen())
    print(result)