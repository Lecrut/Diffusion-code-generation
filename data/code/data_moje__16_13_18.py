def get_first_from_generator(gen):
    return next(gen)

if __name__ == '__main__':
    def sample_gen():
        yield 10
        yield 20
        yield 30

    result = get_first_from_generator(sample_gen())
    print(result)