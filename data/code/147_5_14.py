def sort_tuples(data):
    if not data:
        return []
    return sorted(data, key=lambda x: (x[1], x[0]))

if __name__ == '__main__':
    sample_list_1 = [(3, 2), (1, 1), (4, 1), (2, 3)]
    sample_list_2 = []
    sample_list_3 = [(5, -1), (-2, -1), (0, 0), (3, 2)]
    
    print("Sample 1:", sort_tuples(sample_list_1))
    print("Sample 2:", sort_tuples(sample_list_2))
    print("Sample 3:", sort_tuples(sample_list_3))