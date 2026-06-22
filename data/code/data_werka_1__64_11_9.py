def find_final_item_index(item_indices):
    index_map = {0: -1}
    if len(item_indices) > 0:
        index_map[len(item_indices)] = item_indices[-1]
    return index_map.get(len(item_indices), -1)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    result1 = find_final_item_index(list1)
    print(result1)
    list2 = [100]
    result2 = find_final_item_index(list2)
    print(result2)
    list3 = []
    result3 = find_final_item_index(list3)
    print(result3)
    list4 = [42]
    result4 = find_final_item_index(list4)
    print(result4)