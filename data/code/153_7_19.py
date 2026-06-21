def is_item_in_nested_list(item, nested_list):
    for element in nested_list:
        if element == item:
            return True
        elif isinstance(element, list):
            if is_item_in_nested_list(item, element):
                return True
    return False
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6], 7], 8]
    print(is_item_in_nested_list(5, sample_list))
    print(is_item_in_nested_list(9, sample_list))