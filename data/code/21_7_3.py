def sort_by_custom_rule(data_list, key_index):
    return sorted(data_list, key=lambda item: item[key_index], reverse=True)
if __name__ == '__main__':
    sample_data = [
        (10, 1),
        (5, 2),
        (20, 3),
        (15, 4)
    ]
    key = 0
    sorted_data = sort_by_custom_rule(sample_data, key)
    print(f"Original Data: {sample_data}")
    print(f"Sorting by index {key} in descending order:")
    print(f"Sorted Data: {sorted_data}")
    sample_data_2 = [
        (30, 0),
        (10, 1),
        (20, 2),
        (15, 3)
    ]
    key_2 = 1
    sorted_data_2 = sort_by_custom_rule(sample_data_2, key_2)
    print(f"\nOriginal Data: {sample_data_2}")
    print(f"Sorting by index {key_2} in descending order:")
    print(f"Sorted Data: {sorted_data_2}")