def are_elements_unique(lst):
    seen = set()
    for item in lst:
        if item in seen:
            return False
        seen.add(item)
    return True

if __name__ == '__main__':
    sample_list1 = [7, 9, 3, 5, 8]
    print(are_elements_unique(sample_list1))
    
    sample_list2 = [4, 6, 2, 6, 0]
    print(are_elements_unique(sample_list2))