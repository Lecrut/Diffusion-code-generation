def merge_lists(list1, list2):
    seen = set()
    result = []
    for item in list1 + list2:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1.0, 2.0, 3.0]
    sample_list2 = [3.0, 4.0, 5.0]
    merged_list = merge_lists(sample_list1, sample_list2)
    print(merged_list)