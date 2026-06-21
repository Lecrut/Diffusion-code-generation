def find_common_elements(list1, list2):
    common = []
    for item in list1:
        if item in list2 and item not in common:
            common.append(item)
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    result1 = find_common_elements(sample_list1, sample_list2)
    print(f"Common elements between {sample_list1} and {sample_list2}: {result1}")
    sample_list3 = [10, 20, 30, 40]
    sample_list4 = [30, 40, 50, 60]
    result2 = find_common_elements(sample_list3, sample_list4)
    print(f"Common elements between {sample_list3} and {sample_list4}: {result2}")
    sample_list5 = ['a', 'b', 'c', 'd']
    sample_list6 = ['c', 'd', 'e', 'f']
    result3 = find_common_elements(sample_list5, sample_list6)
    print(f"Common elements between {sample_list5} and {sample_list6}: {result3}")