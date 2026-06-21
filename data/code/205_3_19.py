def sort_tuple_to_list(data):
    sorted_list = []
    while data:
        min_value = min(data)
        sorted_list.append(min_value)
        data = data.replace((min_value,), ())
    return sorted_list

if __name__ == '__main__':
    sample_data = (3, 1, 5, 2, 8)
    sorted_result = sort_tuple_to_list(sample_data)
    print(sorted_result)