def sort_tuples_by_second_element(tuples_list):
    if not all(isinstance(item, tuple) and len(item) == 2 for item in tuples_list):
        raise ValueError("All elements must be tuples of length 2")
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(7, 2), (3, 5), (8, 2), (6, 1)]
    try:
        sorted_tuples = sort_tuples_by_second_element(sample_tuples)
        print(sorted_tuples)
    except ValueError as e:
        print(e)