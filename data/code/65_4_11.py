def index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item

if __name__ == '__main__':
    sample_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target_index = 5
    for value in index_generator(sample_list, target_index):
        print(value)