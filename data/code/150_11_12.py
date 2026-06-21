def filter_list(input_list, item_to_remove):
    return [item for item in input_list if item != item_to_remove]

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 20, 60]
    value_to_filter = 20
    filtered_result = filter_list(sample_data, value_to_filter)
    print(f"Original list: {sample_data}")
    print(f"Value to remove: {value_to_filter}")
    print(f"Filtered list: {filtered_result}")