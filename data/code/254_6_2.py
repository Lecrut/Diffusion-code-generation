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
    print("Data 1:", list(find_minimum_generator(data1)))
    data2 = [10, 4, 7, 1, 12, 6]
    print("Data 2:", list(find_minimum_generator(data2)))
    data3 = [50, 40, 30, 20, 10]
    print("Data 3:", list(find_minimum_generator(data3)))
    data4 = [7]
    print("Data 4:", list(find_minimum_generator(data4)))
    data5 = []
    print("Data 5:", list(find_minimum_generator(data5)))