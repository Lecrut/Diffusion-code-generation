def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            last = next(iterator)
    except StopIteration:
        yield last

if __name__ == '__main__':
    sample_iterable = {'a': 1, 'b': 2, 'c': 3}
    for last_item in last_item_generator(sample_iterable.values()):
        print(last_item)