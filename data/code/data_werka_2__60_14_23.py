def get_final_item(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    try:
        return arr[-1]
    except IndexError:
        raise ValueError("List cannot be empty")

if __name__ == '__main__':
    sample_list = [7, 8, 9, 10, 11]
    print(get_final_item(sample_list))
    
    empty_list = []
    try:
        print(get_final_item(empty_list))
    except ValueError as e:
        print(e)
    
    single_element_list = [42]
    print(get_final_item(single_element_list))