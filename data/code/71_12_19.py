def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list1 = [5, 3, 8, 6, 7]
    print("Middle element of", sample_list1, "is:", find_middle_element(sample_list1))
    
    sample_list2 = [1, 4, 9, 16, 25, 36]
    print("Middle element of", sample_list2, "is:", find_middle_element(sample_list2))