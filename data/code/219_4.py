def find_max_generator(iterable):
    try:
        iterator = iter(iterable)
        first_item = next(iterator)
    except StopIteration:
        return
    current_max = first_item
    yield current_max
    for item in iterator:
        if item > current_max:
            current_max = item
        yield current_max
if __name__ == '__main__':
    data1 = [3, 1, 4, 1, 5, 9, 2]
    print("Data 1:")
    for max_val in find_max_generator(data1):
        print(max_val)
    data2 = [10, 7, 20, 3, 15]
    print("\nData 2:")
    for max_val in find_max_generator(data2):
        print(max_val)
    data3 = [-5, -1, -10, -2]
    print("\nData 3:")
    for max_val in find_max_generator(data3):
        print(max_val)
    data4 = [42]
    print("\nData 4:")
    for max_val in find_max_generator(data4):
        print(max_val)
    data5 = []
    print("\nData 5 (Empty):")
    for max_val in find_max_generator(data5):
        print(max_val)