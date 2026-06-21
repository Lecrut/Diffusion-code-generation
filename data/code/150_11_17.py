def filter_list(items, value_to_exclude):
    filtered_items = [item for item in items if item != value_to_exclude]
    return filtered_items

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50, 20, 60, 70, 80, 90, 20]
    value_to_exclude = 20
    result = filter_list(sample_data, value_to_exclude)
    print(f"Original list: {sample_data}")
    print(f"Value to exclude: {value_to_exclude}")
    print(f"Filtered list: {result}")