def validate_tuples(tuples_list):
    if not isinstance(tuples_list, list):
        raise ValueError("Input must be a list of tuples.")
    for item in tuples_list:
        if not isinstance(item, tuple) or len(item) != 2:
            raise ValueError("All elements must be tuples of length 2.")

def sort_tuples_by_second_element(tuples_list):
    validate_tuples(tuples_list)
    return sorted(tuples_list, key=lambda x: x[1])

if __name__ == '__main__':
    sample_values = [(7, 5), (3, 2), (9, 8), (4, 2)]
    sorted_values = sort_tuples_by_second_element(sample_values)
    print(sorted_values)