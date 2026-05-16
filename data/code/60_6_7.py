def last_item_generator(iterable):
    it = iter(iterable)
    last_item = None
    try:
        while True:
            last_item = next(it)
    except StopIteration:
        if last_item is not None:
            yield last_item
    else:
        pass
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    gen = last_item_generator(data)
    result = None
    try:
        result = next(gen)
    except StopIteration:
        pass
    print(result)
    data_empty = []
    gen_empty = last_item_generator(data_empty)
    result_empty = None
    try:
        result_empty = next(gen_empty)
    except StopIteration:
        pass
    print(result_empty)
    data_single = [99]
    gen_single = last_item_generator(data_single)
    result_single = None
    try:
        result_single = next(gen_single)
    except StopIteration:
        pass
    print(result_single)