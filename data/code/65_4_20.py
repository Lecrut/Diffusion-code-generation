def index_generator(iterable, index):
    for i, item in enumerate(iterable):
        if i == index:
            yield item

if __name__ == '__main__':
    SAMPLE_ITERABLE = range(1000000)
    TARGET_INDEX = 500000
    result = list(index_generator(SAMPLE_ITERABLE, TARGET_INDEX))
    print(result)