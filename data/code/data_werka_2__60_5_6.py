def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            item = next(iterator)
    except StopIteration:
        yield None

if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    generator = last_item_generator(sample_iterable)
    print(next(generator))