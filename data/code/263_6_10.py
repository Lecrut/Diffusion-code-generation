def sort_tuples_by_second_element(tuples):
    return sorted(tuples, key=lambda x: x[1], reverse=True)

if __name__ == '__main__':
    sample_data = [(1, 2), (3, 1), (5, 0), (7, 4)]
    sorted_data = sort_tuples_by_second_element(sample_data)
    print(sorted_data)