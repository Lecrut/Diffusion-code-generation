def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))

if __name__ == '__main__':
    sample_list1 = ["Apple", "Banana", "Cherry", "Date"]
    sample_list2 = ["Banana", "Elderberry", "Fig", "Grape"]
    print(find_common_elements(sample_list1, sample_list2))