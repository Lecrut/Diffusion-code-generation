def merge_lists(list1, list2):
    seen = set()
    merged_list = []
    for item in list1:
        if item not in seen:
            seen.add(item)
            merged_list.append(item)
    for item in list2:
        if item not in seen:
            seen.add(item)
            merged_list.append(item)
    return merged_list

if __name__ == '__main__':
    sample_list_a = [1.0, 2.0, 3.0]
    sample_list_b = [3.0, 4.0, 5.0]
    result = merge_lists(sample_list_a, sample_list_b)
    print(result)