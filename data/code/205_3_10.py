def validate_input(data):
    if not isinstance(data, tuple):
        raise ValueError("Input must be a tuple")
    for item in data:
        if not isinstance(item, int):
            raise ValueError("All elements of the tuple must be integers")

def sort_tuple_to_list(input_tuple):
    validate_input(input_tuple)
    sorted_list = []
    while input_tuple:
        min_value = min(input_tuple)
        sorted_list.append(min_value)
        input_tuple = input_tuple[:input_tuple.index(min_value)] + input_tuple[input_tuple.index(min_value) + 1:]
    return sorted_list

if __name__ == '__main__':
    sample_data = (3, 1, 4, 1, 5, 9, 2, 6, 5)
    sorted_result = sort_tuple_to_list(sample_data)
    print(sorted_result)