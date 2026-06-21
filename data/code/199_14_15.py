def merge_and_sort_names(list1, list2):
    merged_list = list1 + list2
    cleaned_set = {name.strip() for name in merged_list}
    return sorted(cleaned_set)

if __name__ == '__main__':
    sample_list1 = ["Alice ", "Bob", "Charlie"]
    sample_list2 = [" bob", "Dave", "Eve  "]
    result = merge_and_sort_names(sample_list1, sample_list2)
    print(result)