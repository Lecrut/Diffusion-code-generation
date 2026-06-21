def merge_lists(list1, list2):
    seen = set()
    merged_list = []
    for item in list1 + list2:
        if item not in seen:
            seen.add(item)
            merged_list.append(item)
    return merged_list

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [3.3, 4.4, 5.5, 6.6]
    result = merge_lists(sample_list1, sample_list2)
    print(result)