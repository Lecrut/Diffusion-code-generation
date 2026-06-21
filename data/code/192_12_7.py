def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(intersection)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [30, 40, 50, 60, 70]
    print(find_common_elements(sample_list1, sample_list2))