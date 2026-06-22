def sort_tuples_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 4), (5, 6), (7, 8)]
    print(sort_tuples_by_second_element(sample_data))