def get_list_elements(lst):
    if not lst:
        return ()
    first_element = lst[0]
    last_element = lst[-1]
    middle_index = len(lst) // 2
    middle_element = lst[middle_index]
    return (first_element, last_element, middle_element)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    result = get_list_elements(sample_list)
    print(result)