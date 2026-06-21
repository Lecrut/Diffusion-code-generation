def merge_lists(list1, list2):
    seen = set()
    result = []
    for item in list1 + list2:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3]
    sample_list2 = [3.3, 4.4, 5.5]
    merged_result = merge_lists(sample_list1, sample_list2)
    print(merged_result)