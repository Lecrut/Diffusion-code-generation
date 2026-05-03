def last_item_generator(iterable):
    it = iter(iterable)
    last_item = None
    try:
        while True:
            last_item = next(it)
    except StopIteration:
        if last_item is not None:
            yield last_item
    finally:
        return
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    gen = last_item_generator(data)
    result = None
    for item in gen:
        result = item
    print(result)
    data_empty = []
    gen_empty = last_item_generator(data_empty)
    result_empty = None
    for item in gen_empty:
        result_empty = item
    print(result_empty)
    data_single = [99]
    gen_single = last_item_generator(data_single)
    result_single = None
    for item in gen_single:
        result_single = item
    print(result_single)