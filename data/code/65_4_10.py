def index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item
if __name__ == '__main__':
    sample_sequence = range(1000000)
    target_index = 500000
    result = list(index_generator(sample_sequence, target_index))
    print(result)