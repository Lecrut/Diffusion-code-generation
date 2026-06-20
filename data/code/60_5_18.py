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
    sample_iterable = ['a', 'b', 'c']
    generator = last_item_generator(sample_iterable)
    print(next(generator))