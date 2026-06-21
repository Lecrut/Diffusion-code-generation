def set_difference(list1, list2):
    diff = []
    for item in list1:
        if not any(item == x for x in list2):
            diff.append(item)
    return diff

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 1]
    sample_list2 = [4, 7, 8, 1]
    result = set_difference(sample_list1, sample_list2)
    print(result)