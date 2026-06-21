def contains_item(lst, value):
    if not isinstance(lst, list) or not all(isinstance(item, (int, str)) for item in lst):
        raise ValueError("lst must be a list of integers or strings")
    if not isinstance(value, (int, str)):
        raise ValueError("value must be an integer or string")
    
    return value in set(lst)

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    search_value = 30
    print(contains_item(sample_list, search_value))