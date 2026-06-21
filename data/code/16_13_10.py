def get_first_element(generator):
    return next(generator)

if __name__ == '__main__':
    def sample_generator():
        yield 1
        yield 2
        yield 3

    gen = sample_generator()
    result = get_first_element(gen)
    print(result)