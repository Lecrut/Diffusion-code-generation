def find_middle_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    n = len(lst)
    middle_index = n // 2
    return lst[middle_index]

if __name__ == '__main__':
    sample_list = [1.5, 2.3, 3.7, 4.9]
    print(find_middle_element(sample_list))