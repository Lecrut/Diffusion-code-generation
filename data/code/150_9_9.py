def is_item_in_list(lst, item):
    return item in lst

def safe_remove_item(lst, item):
    if not is_item_in_list(lst, item):
        raise TypeError("Item not found in list")
    
    try:
        lst.remove(item)
    except ValueError as e:
        raise TypeError(f"Error removing item: {e}")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    item_to_remove = 3
    try:
        safe_remove_item(sample_list, item_to_remove)
        print(sample_list)
    except TypeError as e:
        print(e)