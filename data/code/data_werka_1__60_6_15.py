def get_last_element(lst):
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    try:
        return lst[-1]
    except IndexError:
        return None

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = []
    sample_list_3 = ['a', 'b', 'c']
    
    print("Last element of sample_list_1:", get_last_element(sample_list_1))
    print("Last element of sample_list_2:", get_last_element(sample_list_2))
    print("Last element of sample_list_3:", get_last_element(sample_list_3))