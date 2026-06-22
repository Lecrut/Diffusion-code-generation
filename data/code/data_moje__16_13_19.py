def get_first_element(iterator):
    try:
        return next(iterator)
    except StopIteration:
        return None

if __name__ == '__main__':
    def number_generator():
        yield 10
        yield 20
        yield 30

    gen = number_generator()
    first_item = get_first_element(gen)
    print(first_item)