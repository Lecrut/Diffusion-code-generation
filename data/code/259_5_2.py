def find_min_max_generator(iterable):
    try:
        first_item = next(iter(iterable))
    except StopIteration:
        return
    current_min = first_item
    current_max = first_item
    for item in iterable:
        if item < current_min:
            current_min = item
        elif item > current_max:
            current_max = item
    yield current_min
    yield current_max
if __name__ == '__main__':
    data1 = [5, 1, 9, 3, 7, 2, 8]
    print("Data 1:", list(find_min_max_generator(data1)))
    data2 = [100, 50, 200, 10, 150]
    print("Data 2:", list(find_min_max_generator(data2)))
    data3 = [42]
    print("Data 3:", list(find_min_max_generator(data3)))
    data4 = []
    print("Data 4 (Empty):", list(find_min_max_generator(data4)))