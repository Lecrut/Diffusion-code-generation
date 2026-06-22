def validate_input(tuples_list):
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list.")
    for item in tuples_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("All elements of the list must be tuples of length 2.")

def sort_tuples_by_second_element(tuples_list):
    validate_input(tuples_list)
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(5, 4), (3, 2), (8, 2), (1, 6)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)