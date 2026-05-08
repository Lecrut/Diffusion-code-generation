def sort_tuples(data):
    return sorted(data, key=lambda item: (item[1], -item[0]))
if __name__ == '__main__':
    data = [(3, 5), (1, 8), (3, 2), (1, 5), (4, 8)]
    sorted_data = sort_tuples(data)
    print(sorted_data)