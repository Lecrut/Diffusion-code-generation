def find_final_item_index(item_indices):
    index_map = {True: -1, False: len(item_indices) - 1}
    return index_map[not item_indices]

if __name__ == '__main__':
    list1 = [7, 3, 9, 2]
    result1 = find_final_item_index(list1)
    print(result1)
    
    list2 = [45]
    result2 = find_final_item_index(list2)
    print(result2)
    
    list3 = []
    result3 = find_final_item_index(list3)
    print(result3)
    
    list4 = [99, 88, 77]
    result4 = find_final_item_index(list4)
    print(result4)