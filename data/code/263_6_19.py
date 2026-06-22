def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [(1, 3), (4, 1), (2, 9), (7, 5)]
    sorted_data = sort_by_second_element(sample_data)
    print(sorted_data)