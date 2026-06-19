def find_final_item_index(lst, item):
    try:
        indices = (i for i, x in enumerate(lst) if x == item)
        return max(indices, default=-1)
    except TypeError:
        raise ValueError('The first argument must be a list')
if __name__ == '__main__':
    assert find_final_item_index([], 5) == -1, 'Test case 1 failed'
    assert find_final_item_index([1, 2, 3, 4], 5) == -1, 'Test case 2 failed'
    assert find_final_item_index([1, 2, 3, 4, 3], 3) == 4, 'Test case 3 failed'
    assert find_final_item_index(['a', 'b', 'c', 'b'], 'b') == 3, 'Test case 4 failed'
    assert find_final_item_index([1, 2, 3, 4, 5], 6) == -1, 'Test case 5 failed'
    assert find_final_item_index(['a', 'b', 'c', 'a'], 'a') == 3, 'Test case 6 failed'
    sample_list = [10, 20, 30, 40, 50, 30]
    item_to_find = 30
    index = find_final_item_index(sample_list, item_to_find)
    print(index)