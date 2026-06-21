def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_values = [(7, 2), (3, 4), (5, 2), (1, 3), (9, 1)]
    sorted_result = sort_tuples_by_second_element(sample_values)
    print(sorted_result)