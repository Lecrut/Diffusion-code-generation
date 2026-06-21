def remove_last_element(data_list):
    if data_list:
        data_list.pop(-1)
    return data_list

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4]
    print("Original list:", sample_list)
    result = remove_last_element(sample_list)
    print("List after removing last element:", result)

    empty_list = []
    print("\nEmpty list:", empty_list)
    result = remove_last_element(empty_list)
    print("Result of attempting to remove from an empty list:", result)