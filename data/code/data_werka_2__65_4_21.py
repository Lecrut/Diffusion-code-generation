def positional_index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item
if __name__ == '__main__':
    sample_iterable = [10, 20, 30, 40, 50]
    target_index = 2
    generator = positional_index_generator(sample_iterable, target_index)
    for element in generator:
        print(element)