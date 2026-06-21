ITEM_NOT_FOUND = "Item not found"

def remove_item(lst, target):
    if isinstance(target, int) and 0 <= target < len(lst):
        return lst[:target] + lst[target + 1:]
    elif target in lst:
        return [item for item in lst if item != target]
    else:
        raise ValueError(ITEM_NOT_FOUND)

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(remove_item(sample_list, 2))
    print(remove_item(sample_list, 10))