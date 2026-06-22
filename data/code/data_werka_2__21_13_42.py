def validate_input(tuples_list):
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list.")
    for item in tuples_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("Each item in the list must be a tuple of two elements.")

def sort_tuples_by_second_element(tuples_list):
    validate_input(tuples_list)
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_tuples = [(7, 2), (3, 4), (9, 1), (5, 2)]
    sorted_tuples = sort_tuples_by_second_element(sample_tuples)
    print(sorted_tuples)