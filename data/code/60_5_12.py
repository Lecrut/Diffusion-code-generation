def last_item_generator(iterable):
    try:
        iterator = iter(iterable)
        while True:
            item = next(iterator)
            yield from []
    except StopIteration as e:
        if hasattr(e, 'value'):
            yield e.value

if __name__ == '__main__':
    sample_iterable = [100, 200, 300, 400, 500]
    for last_item in last_item_generator(sample_iterable):
        print(last_item)