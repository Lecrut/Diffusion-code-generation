def merge_and_sort_names(list1, list2):
    merged_list = list1 + list2
    unique_set = set(name.strip() for name in merged_list)
    sorted_list = sorted(unique_set)
    return sorted_list

if __name__ == '__main__':
    sample_list1 = ["Alice ", "Bob", "Charlie"]
    sample_list2 = ["Dave ", "Eve", "Alice"]
    result = merge_and_sort_names(sample_list1, sample_list2)
    print(result)