def merge_and_sort_names(list1, list2):
    merged = set(name.strip() for name in list1 + list2)
    return sorted(merged)

if __name__ == '__main__':
    sample_list1 = ["Alice ", "Bob", "Charlie"]
    sample_list2 = ["Anna", "David ", "Betty"]
    result = merge_and_sort_names(sample_list1, sample_list2)
    print(result)