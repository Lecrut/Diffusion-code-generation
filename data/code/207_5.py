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
    print(list(find_max_generator(data1)))
    data2 = [-5, -1, -10, -2]
    print(list(find_max_generator(data2)))
    data3 = [42]
    print(list(find_max_generator(data3)))
    data4 = []
    print(list(find_max_generator(data4)))