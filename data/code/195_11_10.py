def intersect_lists(list1, list2):
    set2 = set(list2)
    result = []
    for item in list1:
        if item in set2 and item not in result:
            result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5, 5, 6]
    sample_list2 = [4, 5, 6, 7, 8, 9]
    print(intersect_lists(sample_list1, sample_list2))