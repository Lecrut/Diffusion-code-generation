def get_third_item(lst: list) -> object:
    if not isinstance(lst, list):
        raise TypeError("Input must be a list")
    if len(lst) < 3:
        raise IndexError("List does not have a third item")
    return lst[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    third_item = get_third_item(sample_list)
    print(third_item)
    
    try:
        get_third_item([1, 2])
    except IndexError as e:
        print(f"Caught IndexError: {e}")
    
    try:
        get_third_item("not a list")
    except TypeError as e:
        print(f"Caught TypeError: {e}")