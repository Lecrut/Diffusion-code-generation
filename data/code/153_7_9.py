def item_exists(nested_list, target):
    for item in nested_list:
        if isinstance(item, list):
            if item_exists(item, target):
                return True
        elif item == target:
            return True
    return False
if __name__ == '__main__':
    sample_list = [1, 2, [3, 4, [5, 6]], 7]
    print(item_exists(sample_list, 5))
    print(item_exists(sample_list, 8))