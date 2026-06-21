def find_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [40, 50, 60, 70, 80]
    common_items = find_common_items(sample_list1, sample_list2)
    print(f"Common items between {sample_list1} and {sample_list2}: {common_items}")

    sample_list3 = ['apple', 'banana', 'cherry']
    sample_list4 = ['banana', 'date', 'apple']
    common_items = find_common_items(sample_list3, sample_list4)
    print(f"Common items between {sample_list3} and {sample_list4}: {common_items}")

    sample_list5 = [1.1, 2.2, 3.3]
    sample_list6 = [3.3, 4.4, 5.5]
    common_items = find_common_items(sample_list5, sample_list6)
    print(f"Common items between {sample_list5} and {sample_list6}: {common_items}")