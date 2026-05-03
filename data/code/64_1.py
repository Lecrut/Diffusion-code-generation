def find_final_index(data_list, target_item):
    last_index = -1
    for i in range(len(data_list)):
        if data_list[i] == target_item:
            last_index = i
    return last_index
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
    list4 = [7, 7, 7, 7]
    target4 = 7
    result4 = find_final_index(list4, target4)
    print(f"List: {list4}, Target: {target4}, Final Index: {result4}")
    list5 = []
    target5 = 1
    result5 = find_final_index(list5, target5)
    print(f"List: {list5}, Target: {target5}, Final Index: {result5}")