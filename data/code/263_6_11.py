def sort_tuples_by_second_element_desc(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 1), (4, 5), (2, 3)]
    print(sort_tuples_by_second_element_desc(sample_data))