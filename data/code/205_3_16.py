def sort_tuple_into_list(data):
    sorted_list = []
    while data:
        min_value = min(data)
        sorted_list.append(min_value)
        data.remove(min_value)
    return sorted_list

if __name__ == '__main__':
    sample_data = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
    sorted_result = sort_tuple_into_list(sample_data)
    print(sorted_result)