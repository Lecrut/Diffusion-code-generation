def get_first_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    return lst[0] if lst else None

if __name__ == '__main__':
    sample_list_1 = [42, 73, 99]
    empty_list = []
    sample_list_2 = ['apple', 'banana', 'cherry']
    
    first_element_1 = get_first_element(sample_list_1)
    first_element_2 = get_first_element(empty_list)
    first_element_3 = get_first_element(sample_list_2)
    
    print("First element of sample_list_1:", first_element_1)
    print("First element of empty_list:", first_element_2)
    print("First element of sample_list_2:", first_element_3)