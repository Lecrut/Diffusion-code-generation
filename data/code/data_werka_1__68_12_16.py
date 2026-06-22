def find_difference(list1: list, list2: list) -> list:
    set1 = set(list1)
    set2 = set(list2)
    
    if not set1:
        return []
    
    difference_set = set1 - set2
    return list(difference_set)

if __name__ == '__main__':
    sample_list1 = [5, 10, 15, 20, 25]
    sample_list2 = [10, 20, 30, 40, 50]
    result = find_difference(sample_list1, sample_list2)
    print(result)