def find_minimum_generator(sequence):
    if not sequence:
        return
    current_min = sequence[0]
    yield current_min
    for item in sequence[1:]:
        if item < current_min:
            current_min = item
            yield current_min
if __name__ == '__main__':
    data1 = [5, 2, 8, 1, 9, 3]
    print("Minimum for data1:", list(find_minimum_generator(data1)))
    data2 = [10, 4, 15, 2, 7]
    print("Minimum for data2:", list(find_minimum_generator(data2)))
    data3 = [50, 40, 30, 20]
    print("Minimum for data3:", list(find_minimum_generator(data3)))
    data4 = [100]
    print("Minimum for data4:", list(find_minimum_generator(data4)))
    data5 = []
    print("Minimum for data5:", list(find_minimum_generator(data5)))