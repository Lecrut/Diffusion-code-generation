def index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item
if __name__ == '__main__':
    sample_iterable = range(1000000)
    target_index = 500000
    generator = index_generator(sample_iterable, target_index)
    for element in generator:
        print(element)