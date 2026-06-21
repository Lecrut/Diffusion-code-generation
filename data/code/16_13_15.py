def get_first_generator_element(gen):
    try:
        return next(gen)
    except StopIteration:
        raise ValueError("Generator is empty")

if __name__ == "__main__":
    def sample_generator():
        yield 10
        yield 20
        yield 30

    gen_obj = sample_generator()
    first_item = get_first_generator_element(gen_obj)
    print(first_item)
    print(get_first_generator_element(iter([5, 15, 25])))
    try:
        get_first_generator_element(iter([]))
    except ValueError as e:
        print(e)