def contains_item(data_list: list, target_item) -> bool:
    return target_item in set(data_list)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    target1 = 8
    result1 = contains_item(list1, target1)
    print(f"List: {list1}, Target: {target1}, Result: {result1}")

    list2 = ['a', 'b', 'c', 'd']
    target2 = 'e'
    result2 = contains_item(list2, target2)
    print(f"List: {list2}, Target: {target2}, Result: {result2}")

    list3 = [1000000, 2000000]
    target3 = 1000000
    result3 = contains_item(list3, target3)
    print(f"List: {list3}, Target: {target3}, Result: {result3}")