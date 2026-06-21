def index_generator(iterable, index):
    try:
        yield iterable[index]
    except IndexError:
        raise ValueError("Index out of range")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    index_to_fetch = 2
    result = list(index_generator(sample_list, index_to_fetch))
    print(result)