def extend_lists(list1, list2):
    extended_list = list1.copy()
    extended_list.extend(list2)
    return extended_list

if __name__ == '__main__':
    sample_list_a = ["apple", "banana"]
    sample_list_b = ["cherry", "date"]
    result = extend_lists(sample_list_a, sample_list_b)
    print(result)