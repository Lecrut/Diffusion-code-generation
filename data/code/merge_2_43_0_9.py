def remove_by_value(lst: list, value) -> bool:
    try:
        lst.remove(value)
        return True
    except ValueError:
        return False
def remove_by_index(lst: list, index: int) -> bool:
    if 0 <= index < len(lst):
        del lst[index]
        return True
    return False
if __name__ == '__main__':
    sample_list = [1, 'apple', 3.14, 'banana', 5]
    removed_by_value = remove_by_value(sample_list.copy(), 'apple')
    original_len_before_index_removal = len([x for x in sample_list if not isinstance(x, str)]) + sum(1 for _ in [sample_list[0]])
    removed_by_index = remove_by_index(sample_list.copy(), 2)
    print(f"Removed by value: {removed_by_value}")
    print(f"List after removing 'apple': {[x for x in sample_list if not isinstance(x, str)] + ['banana']}")                                                             
    test_data = [10, 20, 'target', 40]
    print(f"Original data: {test_data}")
    if remove_by_value(test_data.copy(), 'target'):
        print("Value removed successfully.")
    test_data_2 = [10, 20, 30, 40]
    original_len_before_index_removal = len([x for x in test_data_2 if not isinstance(x, str)]) + sum(1 for _ in [test_data_2[0]])                                          
    removed_by_idx = remove_by_index(test_data_2.copy(), 3)
    print(f"Removed by index: {removed_by_idx}")