def contains_item(lst, value):
    if not isinstance(lst, list):
        raise ValueError("First argument must be a list")
    if not isinstance(value, (int, str)):
        raise ValueError("Second argument must be an integer or string")
    
    return value in set(lst)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    search_value = 3
    print(contains_item(sample_list, search_value))
    print(contains_item(['apple', 'banana'], 'apple'))
    try:
        contains_item('not a list', 3)
    except ValueError as e:
        print(e)