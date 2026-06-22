def find_final_index(data_list, target_item):
    index_map = {}
    for index, item in enumerate(data_list):
        if item == target_item:
            index_map[item] = index
    return index_map.get(target_item, -1)

if __name__ == '__main__':
    list1 = [1, 2, 3, 2, 4, 2, 5]
    target1 = 2
    result1 = find_final_index(list1, target1)
    print(f"List: {list1}, Target: {target1}, Final Index: {result1}")

    list2 = ['a', 'b', 'c', 'b', 'd', 'b']
    target2 = 'b'
    result2 = find_final_index(list2, target2)
    print(f"List: {list2}, Target: {target2}, Final Index: {result2}")

    list3 = [10, 20, 30, 40]
    target3 = 5
    result3 = find_final_index(list3, target3)
    print(f"List: {list3}, Target: {target3}, Final Index: {result3}")