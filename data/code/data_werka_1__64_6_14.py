def find_final_item_index(lst, item):
    if not lst:
        return -1
    last_index = -1
    for i in range(len(lst)):
        if lst[i] == item:
            last_index = i
    return last_index

if __name__ == '__main__':
    assert find_final_item_index([], 5) == -1, 'Test case 1 failed'
    assert find_final_item_index([1, 2, 3, 4], 5) == -1, 'Test case 2 failed'
    assert find_final_item_index([1, 2, 3, 4, 3], 3) == 4, 'Test case 3 failed'
    assert find_final_item_index(['a', 'b', 'c', 'b'], 'b') == 3, 'Test case 4 failed'
    sample_list = [100, 200, 300, 400, 500, 300]
    item_to_find = 300
    result = find_final_item_index(sample_list, item_to_find)
    print(result)