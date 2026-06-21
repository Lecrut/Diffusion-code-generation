def find_min_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) == 0:
        raise ValueError("List cannot be empty")
    
    min_elem = lst[0]
    for elem in lst:
        if not isinstance(elem, int):
            raise TypeError("All elements in the list must be integers")
        if elem < min_elem:
            min_elem = elem
    return min_elem

if __name__ == '__main__':
    sample_list = [34, 78, 12, 56, 90]
    print(find_min_element(sample_list))