def last_item_generator(iterable):
    it = iter(iterable)
    last_item = None
    try:
        last_item = next(it)
    except StopIteration:
        return
    for item in it:
        last_item = item
        yield last_item
if __name__ == '__main__':
    data = [1, 2, 3, 4, 5]
    gen = last_item_generator(data)
    result = None
    for item in gen:
        result = item
    print(result)
    data2 = [10]
    gen2 = last_item_generator(data2)
    result2 = None
    for item in gen2:
        result2 = item
    print(result2)
    data3 = []
    gen3 = last_item_generator(data3)
    result3 = None
    for item in gen3:
        result3 = item
    print(result3)
    data4 = [99]
    gen4 = last_item_generator(data4)
    result4 = None
    for item in gen4:
        result4 = item
    print(result4)