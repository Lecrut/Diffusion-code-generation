if __name__ == '__main__':
    data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
    sums_of_second_elements = []
    for tup in data:
        sums_of_second_elements.append(tup[1])
    print(sums_of_second_elements)