def find_final_item_index(item_indices):
    if not item_indices:
        return -1
    return item_indices[-1]
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