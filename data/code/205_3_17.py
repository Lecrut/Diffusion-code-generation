def sort_tuple_to_list(data):
    if not isinstance(data, tuple):
        raise ValueError("Input must be a tuple")
    sorted_list = []
    while data:
        min_value = min(data)
        sorted_list.append(min_value)
        data = data.replace((min_value,), ())
    return sorted_list

if __name__ == '__main__':
    sample_data = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
    sorted_result = sort_tuple_to_list(sample_data)
    print(sorted_result)