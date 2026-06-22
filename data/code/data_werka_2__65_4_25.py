def index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item

if __name__ == '__main__':
    sample_sequence = [10, 20, 30, 40, 50]
    target_index = 2
    result = list(index_generator(sample_sequence, target_index))
    print(result)