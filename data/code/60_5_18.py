def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            item = next(iterator)
    except StopIteration:
        yield None
    else:
        yield item

if __name__ == '__main__':
    sample_iterable = [1, 2, 3, 4, 5]
    for last_item in last_item_generator(sample_iterable):
        print(last_item)