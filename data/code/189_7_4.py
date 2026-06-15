import random
def remove_elements(data_list, target):
    i = 0
    while i < len(data_list):
        if data_list[i] == target:
            data_list.pop(i)
        else:
            i += 1
    return data_list
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 5, 3, 5, 9, 4]
    target_value = 5
    print("Original list:", sample_list)
    result_list = remove_elements(sample_list, target_value)
    print("List after removing", target_value, ":", result_list)
    sample_list_2 = [10, 20, 30, 40, 50, 60, 70]
    target_value_2 = 30
    print("\nOriginal list:", sample_list_2)
    result_list_2 = remove_elements(sample_list_2, target_value_2)
    print("List after removing", target_value_2, ":", result_list_2)
    sample_list_3 = [1, 2, 3, 4, 5]
    target_value_3 = 99
    print("\nOriginal list:", sample_list_3)
    result_list_3 = remove_elements(sample_list_3, target_value_3)
    print("List after removing", target_value_3, ":", result_list_3)