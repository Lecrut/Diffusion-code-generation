def get_list_elements(lst):
    if not lst:
        return ()
    
    first_element = lst[0]
    last_element = lst[-1]
    
    length = len(lst)
    middle_index = length // 2
    middle_element = lst[middle_index]
    
    return (first_element, last_element, middle_element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_list_elements(sample_list))