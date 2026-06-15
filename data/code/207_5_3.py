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
    print("Max of data1:", max(find_max_generator(data1)))
    data2 = [-5, -1, -10, -2]
    print("Max of data2:", max(find_max_generator(data2)))
    data3 = [1000, 500, 2000, 100]
    print("Max of data3:", max(find_max_generator(data3)))
    data4 = []
    print("Max of data4 (empty):", find_max_generator(data4))
    data5 = [42]
    print("Max of data5:", max(find_max_generator(data5)))