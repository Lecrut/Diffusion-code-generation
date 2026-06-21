def index_generator(iterable, index):
    if index < 0:
        raise ValueError('Index must be non-negative')
    count = 0
    for item in iterable:
        if count == index:
            yield item
        count += 1
if __name__ == '__main__':
    sample_iterable = range(1000000)
    target_index = 500000
    generator = index_generator(sample_iterable, target_index)
    for value in generator:
        print(value)