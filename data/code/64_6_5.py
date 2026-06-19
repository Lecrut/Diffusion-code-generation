def find_final_item_index(lst, item):
    try:
        return lst.index(item)
    except ValueError:
        return -1
if __name__ == '__main__':
    assert find_final_item_index([], 5) == -1, 'Test case 1 failed'
    assert find_final_item_index([1, 2, 3, 4], 5) == -1, 'Test case 2 failed'
    assert find_final_item_index([1, 2, 3, 4, 3], 3) == 4, 'Test case 3 failed'
    assert find_final_item_index(['a', 'b', 'c', 'a'], 'a') == 3, 'Test case 4 failed'
    sample_list = [10, 20, 30, 40, 50]
    item_to_find = 30
    index = find_final_item_index(sample_list, item_to_find)
    print(index)