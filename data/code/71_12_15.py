def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list1 = [5, 3, 9, 1, 7]
    print("Middle element of", sample_list1, "is:", find_middle_element(sample_list1))
    
    sample_list2 = [8, 4, 6, 2, 0, 3]
    print("Middle element of", sample_list2, "is:", find_middle_element(sample_list2))