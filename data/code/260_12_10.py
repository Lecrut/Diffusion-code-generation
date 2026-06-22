def find_unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.symmetric_difference(set2))

if __name__ == '__main__':
    sample_list1 = [1.1, 2.2, 3.3, 4.4]
    sample_list2 = [3.3, 4.4, 5.5, 6.6]
    print(find_unique_elements(sample_list1, sample_list2))