def find_max_generator(iterable):
    try:
        iterator = iter(iterable)
        try:
            max_val = next(iterator)
        except StopIteration:
            return
        for element in iterator:
            if element > max_val:
                max_val = element
        yield max_val
    except TypeError:
        return
if __name__ == '__main__':
    data1 = [10, 5, 20, 8, 15]
    print("Data 1 Max:")
    for max_val in find_max_generator(data1):
        print(max_val)
    data2 = [-5, -1, -10, -3]
    print("\nData 2 Max:")
    for max_val in find_max_generator(data2):
        print(max_val)
    data3 = []
    print("\nData 3 (Empty):")
    for max_val in find_max_generator(data3):
        print(max_val)
    data4 = [100]
    print("\nData 4 (Single Element):")
    for max_val in find_max_generator(data4):
        print(max_val)