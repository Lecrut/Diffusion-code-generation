def append_lists(list1, list2):
    result = list1[:]
    for item in list2:
        result.append(item)
    return result

if __name__ == '__main__':
    sample_list1 = [3, 6, 9]
    sample_list2 = [12, 15, 18]
    appended_lists = append_lists(sample_list1, sample_list2)
    print(appended_lists)