def find_middle_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    MIDDLE_INDEX_CONSTANT = len(lst) // 2
    return lst[MIDDLE_INDEX_CONSTANT]

if __name__ == '__main__':
    sample_list = [7.1, 8.2, 9.3, 10.4, 11.5]
    print(find_middle_element(sample_list))