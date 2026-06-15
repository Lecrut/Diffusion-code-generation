def min_max_generator(iterable):
    if not iterable:
        return
    current_min = None
    current_max = None
    for item in iterable:
        if current_min is None:
            current_min = item
            current_max = item
        else:
            if item < current_min:
                current_min = item
            if item > current_max:
                current_max = item
        yield current_min, current_max
if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    print("Data 1:")
    for minimum, maximum in min_max_generator(data1):
        print(f"Min: {minimum}, Max: {maximum}")
    data2 = [100, 50, 200, 10, 150]
    print("\nData 2:")
    for minimum, maximum in min_max_generator(data2):
        print(f"Min: {minimum}, Max: {maximum}")
    data3 = [7]
    print("\nData 3:")
    for minimum, maximum in min_max_generator(data3):
        print(f"Min: {minimum}, Max: {maximum}")
    data4 = []
    print("\nData 4 (Empty):")
    for minimum, maximum in min_max_generator(data4):
        print(f"Min: {minimum}, Max: {maximum}")