import random
def remove_elements(data_list, target):
    i = 0
    while i < len(data_list):
        if data_list[i] == target:
            data_list.pop(i)
            if i < len(data_list):
                i -= 1
        i += 1
    return data_list
if __name__ == '__main__':
    sample_list = list(range(1, 21))
    target_value = 5
    print("Original List:", sample_list)
    result_list = remove_elements(sample_list, target_value)
    print("List after removal:", result_list)
    sample_list_2 = [1, 5, 2, 5, 3, 5, 4]
    target_value_2 = 5
    print("\nOriginal List 2:", sample_list_2)
    result_list_2 = remove_elements(sample_list_2, target_value_2)
    print("List 2 after removal:", result_list_2)
    sample_list_3 = [10, 20, 30, 40, 50]
    target_value_3 = 99
    print("\nOriginal List 3:", sample_list_3)
    result_list_3 = remove_elements(sample_list_3, target_value_3)
    print("List 3 after removal:", result_list_3)