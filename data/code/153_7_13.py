def is_item_in_nested_list(item, nested_list):
    for element in nested_list:
        if element == item or (isinstance(element, list) and is_item_in_nested_list(item, element)):
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6]], 7]
    print(is_item_in_nested_list(5, sample_list))
    print(is_item_in_nested_list(8, sample_list))