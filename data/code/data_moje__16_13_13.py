def get_first_element(gen):
    return next(gen, None)

if __name__ == '__main__':
    def sample_generator():
        yield 10
        yield 20
        yield 30

    result = get_first_element(sample_generator())
    print(result)