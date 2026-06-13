def merge_and_sort_strings(list1, list2):
    merged_set = set(list1)
    merged_set.update(list2)
    sorted_list = sorted(list(merged_set))
    return sorted_list
if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry", "apple"]
    list_b = ["date", "banana", "elderberry", "apple"]
    result = merge_and_sort_strings(list_a, list_b)
    print(result)