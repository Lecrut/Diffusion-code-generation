def concatenate_lists(list_a, list_b):
    if not isinstance(list_a, list) or not all(isinstance(item, str) for item in list_a):
        raise ValueError("list_a must be a list of strings")
    if not isinstance(list_b, list) or not all(isinstance(item, str) for item in list_b):
        raise ValueError("list_b must be a list of strings")
    
    return [item for sublist in (list_a, list_b) for item in sublist]

if __name__ == '__main__':
    list_a = ["apple", "banana", "cherry"]
    list_b = ["date", "elderberry", "fig", "apple"]
    result = concatenate_lists(list_a, list_b)
    print(result)