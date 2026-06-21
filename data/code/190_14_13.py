def contains_item(lst, value):
    if not isinstance(lst, list) or not all(isinstance(x, (int, str)) for x in lst):
        raise ValueError("lst must be a list of integers or strings")
    
    if not isinstance(value, (int, str)):
        raise ValueError("value must be an integer or string")
    
    item_set = set(lst)
    return value in item_set

if __name__ == '__main__':
    sample_list = [10, 20, 'apple', 40]
    search_value = 'apple'
    print(contains_item(sample_list, search_value))
    search_value = 30
    print(contains_item(sample_list, search_value))