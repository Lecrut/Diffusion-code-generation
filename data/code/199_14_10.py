def merge_and_sort_names(list1, list2):
    combined = list1 + list2
    unique_sorted = sorted(set(name.strip() for name in combined))
    return unique_sorted

if __name__ == '__main__':
    sample_list1 = ["Alice ", "Bob", "Charlie"]
    sample_list2 = [" bob", "Dave", "Eve  "]
    result = merge_and_sort_names(sample_list1, sample_list2)
    print(result)