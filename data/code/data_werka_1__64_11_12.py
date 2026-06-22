def find_final_item_index(item_indices):
    if not item_indices:
        return -1
    LAST_INDEX = len(item_indices) - 1
    return LAST_INDEX

if __name__ == '__main__':
    list1 = [7, 3, 9, 1]
    result1 = find_final_item_index(list1)
    print(result1)
    list2 = [45]
    result2 = find_final_item_index(list2)
    print(result2)
    list3 = []
    result3 = find_final_item_index(list3)
    print(result3)
    list4 = [89, 67, 45, 23, 12]
    result4 = find_final_item_index(list4)
    print(result4)