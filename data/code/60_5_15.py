def last_item_generator(iterable):
    last_item = None
    for item in iterable:
        last_item = item
    yield last_item

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = last_item_generator(sample_iterable)
    print(next(generator))