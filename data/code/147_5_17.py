def sort_tuples(data):
    if not data:
        return []
    sorted_data = sorted(data, key=lambda x: (x[1], x[0]))
    return sorted_data

if __name__ == '__main__':
    sample_list_1 = [(2, 3), (4, 1), (5, 2)]
    sample_list_2 = []
    sample_list_3 = [(1, -1), (-1, 1), (0, 0)]
    print("Sample 1:", sort_tuples(sample_list_1))
    print("Sample 2:", sort_tuples(sample_list_2))