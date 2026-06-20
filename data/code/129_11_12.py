def sort_tuples(data):
    return sorted(data, key=lambda x: (-x[0], x[1]))

if __name__ == '__main__':
    sample_data = [(3, 2), (1, 4), (3, 1), (2, 3)]
    print(sort_tuples(sample_data))