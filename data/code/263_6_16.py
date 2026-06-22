def sort_by_second_element(tuples_list):
    return sorted(tuples_list, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [(4, 2), (1, 5), (3, 1), (2, 4)]
    sorted_data = sort_by_second_element(sample_data)
    print(sorted_data)