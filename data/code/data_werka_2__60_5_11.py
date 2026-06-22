def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            item = next(iterator)
    except StopIteration:
        yield None

if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    for last_item in last_item_generator(sample_iterable):
        if last_item is not None:
            print(last_item)