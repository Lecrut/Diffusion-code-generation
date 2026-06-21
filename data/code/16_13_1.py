def get_first_generator_element(gen):
    try:
        return next(gen)
    except StopIteration:
        return None

if __name__ == '__main__':
    def sample_generator():
        yield 1
        yield 2
        yield 3

    gen_obj = sample_generator()
    result = get_first_generator_element(gen_obj)
    print(result)

    def empty_generator():
        return
        yield

    empty_gen = empty_generator()
    empty_result = get_first_generator_element(empty_gen)
    print(empty_result)