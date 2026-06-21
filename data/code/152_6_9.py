def is_valid_list(lst):
    return isinstance(lst, list)

def find_common_elements(list_x, list_y):
    if not (is_valid_list(list_x) and is_valid_list(list_y)):
        raise ValueError("Both inputs must be lists")
    
    set_x = set(list_x)
    common_elements = set_x.intersection(set(list_y))
    return list(common_elements)

if __name__ == '__main__':
    list_x = list(range(1, 1000001))
    list_y = list(range(500001, 1500001))
    common_elements = find_common_elements(list_x, list_y)
    print(f"Number of common elements found: {len(common_elements)}")
    print(f"First 10 common elements: {common_elements[:10]}")