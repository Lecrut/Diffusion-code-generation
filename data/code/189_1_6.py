def remove_element(data, value):
    filtered_data = [item for item in data if item != value]
    data[:] = filtered_data

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 2]
    target_value = 2
    print("Original list:", sample_list)
    remove_element(sample_list, target_value)
    print("List after removing all occurrences of", target_value, ":", sample_list)