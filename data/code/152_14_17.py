def find_shared_elements(list1, list2):
    set1 = set(list1)
    common_set = set()
    
    for item in list2:
        if item in set1:
            common_set.add(item)
            
    return list(common_set)

if __name__ == '__main__':
    sample_list1 = [10, 20, 30, 40, 50]
    sample_list2 = [30, 40, 50, 60, 70]
    common_elements = find_shared_elements(sample_list1, sample_list2)
    print(common_elements)