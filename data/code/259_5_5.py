def min_max_generator(iterable):
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
        yield current_min, current_max
if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    print("Data 1:")
    for min_val, max_val in min_max_generator(data1):
        print(f"Min: {min_val}, Max: {max_val}")
    data2 = [100, 50, 200, 10, 300]
    print("\nData 2:")
    for min_val, max_val in min_max_generator(data2):
        print(f"Min: {min_val}, Max: {max_val}")
    data3 = [7]
    print("\nData 3:")
    for min_val, max_val in min_max_generator(data3):
        print(f"Min: {min_val}, Max: {max_val}")
    data4 = []
    print("\nData 4 (Empty):")
    try:
        for min_val, max_val in min_max_generator(data4):
            print(f"Min: {min_val}, Max: {max_val}")
    except StopIteration:
        pass