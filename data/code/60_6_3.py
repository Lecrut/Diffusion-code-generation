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
    result = next(gen)
    print(result)
    data2 = [10]
    gen2 = last_item_generator(data2)
    result2 = next(gen2)
    print(result2)
    data3 = []
    gen3 = last_item_generator(data3)
    try:
        next(gen3)
    except StopIteration:
        pass
    print("Empty list test finished")