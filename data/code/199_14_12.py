def merge_and_unique_names(list1, list2):
    combined_list = list1 + list2
    unique_set = set(name.strip() for name in combined_list)
    sorted_list = sorted(unique_set)
    return sorted_list

if __name__ == '__main__':
    sample_list1 = ["Alice", "Bob ", "Charlie"]
    sample_list2 = ["David", "   Betty ", "Anna"]
    result = merge_and_unique_names(sample_list1, sample_list2)
    print(result)