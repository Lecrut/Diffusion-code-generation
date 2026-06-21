def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[1], tuples_list.index(x)))

if __name__ == '__main__':
    sample_values = [(1, 3), (4, 1), (5, 2), (6, 2), (7, 3)]
    sorted_values = sort_tuples_by_second_element(sample_values)
    print(sorted_values)