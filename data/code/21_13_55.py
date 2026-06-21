def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    SAMPLE_TUPLES = [(7, 2), (3, 4), (9, 1), (5, 2)]
    SORTED_TUPLES = sort_tuples_by_second_element(SAMPLE_TUPLES)
    print(SORTED_TUPLES)