def check_list_item(data_list, target_item):
    return target_item in data_list
if __name__ == '__main__':
    list1 = [1, 5, 8, 12, 3]
    target1 = 8
    result1 = check_list_item(list1, target1)
    print(f"List: {list1}, Target: {target1}, Result: {result1}")
    list2 = ['a', 'b', 'c', 'd']
    target2 = 'e'
    result2 = check_list_item(list2, target2)
    print(f"List: {list2}, Target: {target2}, Result: {result2}")
    list3 = [1000000, 2000000]
    target3 = 1000000
    result3 = check_list_item(list3, target3)
    print(f"List: {list3}, Target: {target3}, Result: {result3}")