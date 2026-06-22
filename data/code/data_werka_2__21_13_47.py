def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_values = [(7, 5), (2, 3), (9, 8), (4, 3), (6, 5)]
    sorted_values = sort_tuples_by_second_element(sample_values)
    print(sorted_values)