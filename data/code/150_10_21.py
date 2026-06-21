def remove_element(lst, item_to_remove):
    if not isinstance(lst, list) or not all(isinstance(x, (int, str)) for x in lst):
        raise ValueError("First argument must be a list of integers or strings")
    
    if not isinstance(item_to_remove, (int, str)):
        raise ValueError("Second argument must be an integer or string")
    
    return [x for x in lst if x != item_to_remove]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    result = remove_element(sample_list, item_to_remove)
    print(result)