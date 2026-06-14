def find_max_generator(iterable):
    try:
        iterator = iter(iterable)
        max_val = next(iterator)
    except StopIteration:
        return
    for element in iterator:
        if element > max_val:
            max_val = element
    yield max_val
if __name__ == '__main__':
    data1 = [10, 5, 20, 8, 30]
    print("Max of data1:", list(find_max_generator(data1)))
    data2 = [-5, -1, -10, -2]
    print("Max of data2:", list(find_max_generator(data2)))
    data3 = [1000]
    print("Max of data3:", list(find_max_generator(data3)))
    data4 = []
    print("Max of data4:", list(find_max_generator(data4)))