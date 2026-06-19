def find_final_item_index(lst, item):
    index = -1
    for i in range(len(lst)):
        if lst[i] == item:
            index = i
    return index

if __name__ == '__main__':
    assert find_final_item_index([], 5) == -1, 'Test case 1 failed'
    assert find_final_item_index([1, 2, 3, 4, 5], 5) == 4, 'Test case 2 failed'
    assert find_final_item_index([1, 2, 3, 4, 5, 3], 3) == 5, 'Test case 3 failed'
    assert find_final_item_index([1, 2, 3, 4, 5], 6) == -1, 'Test case 4 failed'
    assert find_final_item_index(['a', 'b', 'c', 'a'], 'a') == 3, 'Test case 5 failed'
    
    sample_list = [7, 8, 9, 10, 11, 9]
    item_to_find = 9
    result = find_final_item_index(sample_list, item_to_find)
    print(result)