def compare_elements(first_list, second_list, target_index):
    value_from_first = None
    value_from_second = None
    if 0 <= target_index < len(first_list):
        value_from_first = first_list[target_index]
    if 0 <= target_index < len(second_list):
        value_from_second = second_list[target_index]
    return value_from_first, value_from_second

def get_list_lengths(list_one, list_two):
    return len(list_one), len(list_two)

if __name__ == '__main__':
    source_data_a = [100, 200, 300, 400, 500]
    source_data_b = [10.5, 20.5, 30.5]
    query_index = 3
    length_a, length_b = get_list_lengths(source_data_a, source_data_b)
    item_a, item_b = compare_elements(source_data_a, source_data_b, query_index)
    print(f"Index: {query_index}")
    print(f"Lengths: A={length_a}, B={length_b}")
    print(f"Result: ({item_a}, {item_b})")
    invalid_index = 10
    item_c, item_d = compare_elements(source_data_a, source_data_b, invalid_index)
    print(f"Invalid Index Result: ({item_c}, {item_d})")