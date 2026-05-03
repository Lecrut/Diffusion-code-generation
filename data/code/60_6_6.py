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
    data1 = [1, 2, 3, 4, 5]
    print("Data 1:")
    for item in last_item_generator(data1):
        print(item)
    data2 = [10, 20]
    print("\nData 2:")
    for item in last_item_generator(data2):
        print(item)
    data3 = [99]
    print("\nData 3:")
    for item in last_item_generator(data3):
        print(item)
    data4 = []
    print("\nData 4:")
    try:
        for item in last_item_generator(data4):
            print(item)
    except StopIteration:
        pass