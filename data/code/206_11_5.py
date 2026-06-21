def find_min_element(lst):
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise ValueError("Input must be a non-empty list of integers.")
    if len(lst) == 0:
        raise ValueError("List cannot be empty.")
    
    min_element = lst[0]
    for element in lst:
        if element < min_element:
            min_element = element
    return min_element

if __name__ == '__main__':
    sample_list = [3, 5, 1, 2, 4]
    print(find_min_element(sample_list))