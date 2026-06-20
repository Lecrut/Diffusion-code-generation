def sort_dataset(data):
    return sorted(data, key=lambda x: (-x[0], x[1]))

if __name__ == '__main__':
    sample_data = [(3, 2), (1, 5), (3, 1), (2, 4), (1, 3)]
    sorted_data = sort_dataset(sample_data)
    print(sorted_data)