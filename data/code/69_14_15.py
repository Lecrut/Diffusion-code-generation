def get_elements(lst):
    if not lst:
        return ()
    
    first_element = lst[0]
    last_element = lst[-1]
    middle_index = len(lst) // 2
    middle_element = lst[middle_index]
    
    return (first_element, middle_element, last_element)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_elements(sample_list)
    print(result)