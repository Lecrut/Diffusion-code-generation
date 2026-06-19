def index_generator(iterable, index):
    for i, element in enumerate(iterable):
        if i == index:
            yield element
if __name__ == '__main__':
    sample_iterable = range(1000000)
    target_index = 500000
    result = list(index_generator(sample_iterable, target_index))
    print(result)