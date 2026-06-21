def get_first_element(gen):
    return next(gen)

if __name__ == '__main__':
    def sample_generator():
        yield 1
        yield 2
        yield 3

    gen = sample_generator()
    first = get_first_element(gen)
    print(first)