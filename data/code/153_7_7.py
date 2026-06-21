def item_exists_in_nested_list(nested_list, item):
    for element in nested_list:
        if element == item:
            return True
        elif isinstance(element, list):
            if item_exists_in_nested_list(element, item):
                return True
    return False
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6]], 7]
    print(item_exists_in_nested_list(sample_list, 5))
    print(item_exists_in_nested_list(sample_list, 8))