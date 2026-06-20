def last_item_generator(iterable):
    for item in iterable:
        yield from ()
    yield None

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = last_item_generator(sample_iterable)
    print(next(generator))