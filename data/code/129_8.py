def sort_tuples(data):
    return sorted(data, key=lambda item: (item[1], -item[0]))
if __name__ == '__main__':
    data = [(1, 5), (3, 2), (2, 5), (4, 1), (1, 5), (2, 8)]
    sorted_data = sort_tuples(data)
    print(sorted_data)