def last_item_generator(iterable):
    try:
        it = iter(iterable)
        last_item = None
        for item in it:
            last_item = item
        yield last_item
    except StopIteration:
        if iterable:
            yield iterable[-1]
        else:
            pass
if __name__ == '__main__':
    data1 = [1, 2, 3, 4, 5]
    gen1 = last_item_generator(data1)
    result1 = list(gen1)
    print(f"Result 1: {result1}")
    data2 = [10, 20]
    gen2 = last_item_generator(data2)
    result2 = list(gen2)
    print(f"Result 2: {result2}")
    data3 = [99]
    gen3 = last_item_generator(data3)
    result3 = list(gen3)
    print(f"Result 3: {result3}")
    data4 = []
    gen4 = last_item_generator(data4)
    result4 = list(gen4)
    print(f"Result 4: {result4}")