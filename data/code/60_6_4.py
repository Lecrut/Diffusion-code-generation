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
    print(list(last_item_generator(data)))
    data2 = [10]
    print(list(last_item_generator(data2)))
    data3 = []
    print(list(last_item_generator(data3)))
    data4 = [99]
    print(list(last_item_generator(data4)))