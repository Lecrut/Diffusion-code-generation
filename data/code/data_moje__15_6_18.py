def retrieve_second_to_last_item(collection):
    total_count = len(collection)
    target_position = total_count - 2
    return collection[target_position]

if __name__ == '__main__':
    data_set = [100, 200, 300, 400, 500]
    calculated_index = len(data_set) - 2
    output_value = retrieve_second_to_last_item(data_set)
    print(output_value)
    print(data_set[calculated_index])