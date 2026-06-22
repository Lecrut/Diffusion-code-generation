def get_third_item(items: list) -> object:
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    if len(items) < 3:
        raise IndexError("List must contain at least three items")
    return items[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    result = get_third_item(sample_list)
    print(result)
    
    try:
        get_third_item([])
    except IndexError as e:
        print(e)
        
    try:
        get_third_item("not a list")
    except TypeError as e:
        print(e)