def last_item_generator(iterable):
    iterator = iter(iterable)
    try:
        while True:
            item = next(iterator)
    except StopIteration:
        yield item

if __name__ == '__main__':
    sample_iterable = [100, 200, 300, 400, 500]
    for last_item in last_item_generator(sample_iterable):
        print(last_item)