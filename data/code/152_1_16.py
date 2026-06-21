def find_common_elements_ordered(list_a, list_b):
    common = []
    seen = set()
    for item in list_a:
        if item in list_b and item not in seen:
            common.append(item)
            seen.add(item)
    return common

if __name__ == '__main__':
    sample_list1 = [1, 2, 3, 4, 5]
    sample_list2 = [4, 5, 6, 7, 8]
    print(find_common_elements_ordered(sample_list1, sample_list2))
    
    sample_list3 = [10, 20, 30, 40]
    sample_list4 = [30, 40, 50, 60]
    print(find_common_elements_ordered(sample_list3, sample_list4))
    
    sample_list5 = ['a', 'b', 'c', 'd']
    sample_list6 = ['c', 'd', 'e', 'f']
    print(find_common_elements_ordered(sample_list5, sample_list6))