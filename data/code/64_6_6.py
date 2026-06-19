def find_final_item_index(lst, item):
    try:
        return lst.rindex(item)
    except ValueError:
        return -1
if __name__ == '__main__':
    assert find_final_item_index([], 5) == -1, 'Test case 1 failed'
    assert find_final_item_index([1, 2, 3, 4, 5], 5) == 4, 'Test case 2 failed'
    assert find_final_item_index([1, 2, 3, 4, 5, 3], 3) == 5, 'Test case 3 failed'
    assert find_final_item_index([1, 2, 3, 4, 5], 6) == -1, 'Test case 4 failed'
    sample_list = [10, 20, 30, 40, 50, 30]
    item_to_find = 30
    result = find_final_item_index(sample_list, item_to_find)
    print(result)