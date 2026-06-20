def last_item_generator(iterable):
    try:
        last_item = next(iter(iterable))
        for item in iterable:
            last_item = item
        yield last_item
    except StopIteration:
        yield None

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = last_item_generator(sample_iterable)
    print(next(generator))