def remove_item_from_list(input_list, target_item):
    new_list = [item for item in input_list if item != target_item]
    return new_list
if __name__ == '__main__':
    list1 = [1, 2, 3, 2, 4, 2, 5]
    target1 = 2
    result1 = remove_item_from_list(list1, target1)
    print(f"Original list: {list1}")
    print(f"Target item: {target1}")
    print(f"New list: {result1}")
    list2 = ['a', 'b', 'c', 'a', 'd']
    target2 = 'a'
    result2 = remove_item_from_list(list2, target2)
    print(f"Original list: {list2}")
    print(f"Target item: {target2}")
    print(f"New list: {result2}")
    list3 = [10, 20, 30, 40]
    target3 = 5
    result3 = remove_item_from_list(list3, target3)
    print(f"Original list: {list3}")
    print(f"Target item: {target3}")
    print(f"New list: {result3}")