def fetch_final_item(arr):
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    if len(arr) == 0:
        return None
    return arr[-1]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print("Last item in the sample list:", fetch_final_item(sample_list))
    
    empty_list = []
    print("Last item in an empty list:", fetch_final_item(empty_list))
    
    single_element_list = [42]
    print("Last item in a single-element list:", fetch_final_item(single_element_list))