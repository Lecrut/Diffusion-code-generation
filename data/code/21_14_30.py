def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(1, 3), (4, 1), (2, 2), (5, 3)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)