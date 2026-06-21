def remove_element(lst, item_to_remove):
    if not isinstance(lst, list) or not all(isinstance(x, str) for x in lst):
        raise ValueError("Input must be a list of strings.")
    
    return [x for x in lst if x != item_to_remove]

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry', 'date']
    item_to_remove = 'banana'
    result = remove_element(sample_list, item_to_remove)
    print(result)