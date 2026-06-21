def get_elements(lst):
    if not lst:
        return ()
    
    first_element = lst[0]
    last_element = lst[-1]
    middle_index = len(lst) // 2
    middle_element = lst[middle_index]
    
    return (first_element, last_element, middle_element)

if __name__ == '__main__':
    sample_list = [5, 10, 15, 20, 25, 30]
    result = get_elements(sample_list)
    print(result)