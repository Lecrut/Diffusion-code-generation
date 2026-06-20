def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        current_item = next(iterator)
        for item in iterator:
            current_item = item
        yield current_item
    except StopIteration:
        yield None

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    generator = last_item_generator(sample_iterable)
    print(next(generator))