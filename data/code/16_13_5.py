def get_first(generator):
    return next(generator)

if __name__ == '__main__':
    def sample_generator():
        yield 1
        yield 2
        yield 3

    gen = sample_generator()
    print(get_first(gen))