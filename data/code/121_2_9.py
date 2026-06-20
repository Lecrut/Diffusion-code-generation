def compare_lists(list1, list2):
    if len(list1) > len(list2):
        return list1
    elif len(list2) > len(list1):
        return list2
    else:
        return None

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4]
    sample_list2 = [5, 6, 7]
    result = compare_lists(sample_list1, sample_list2)
    print(result)