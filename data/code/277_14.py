def index_iterator(iterable):
    index = 0
    for element in iterable:
        print(index)
        index += 1
if __name__ == '__main__':
    sample_data = (10, 20, 30, 40, 50)
    index_iterator(sample_data)