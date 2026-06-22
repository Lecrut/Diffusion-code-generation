def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: (x[1], tuples_list.index(x)))

if __name__ == '__main__':
    sample_tuples = [(7, 3), (2, 1), (8, 2), (6, 2), (9, 3)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)