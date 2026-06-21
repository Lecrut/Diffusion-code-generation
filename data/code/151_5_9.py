def union_lists(list1, list2):
    seen = set()
    result = []
    for item in list1:
        if item not in seen:
            seen.add(item)
            result.append(item)
    for item in list2:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [3, 4, 5, 6]
    print(union_lists(sample_list1, sample_list2))