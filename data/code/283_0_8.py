def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list1 = [7, 5, 3, 9, 1]
    print(are_elements_unique(sample_list1))
    
    sample_list2 = [8, 6, 4, 2, 0, 5, 3]
    print(are_elements_unique(sample_list2))
    
    sample_list3 = [7, 8, 9, 7, 10]
    print(are_elements_unique(sample_list3))