def remove_item(lst, item):
    if not isinstance(item, type(next(iter(lst)))):
        raise ValueError("Item to remove must be of the same type as list elements")
    return [x for x in lst if x != item]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 2, 5]
    value_to_remove = 2
    try:
        new_list = remove_item(sample_list, value_to_remove)
        print(f"Original list: {sample_list}")
        print(f"Item to remove: {value_to_remove}")
        print(f"New list: {new_list}")
    except ValueError as e:
        print(e)