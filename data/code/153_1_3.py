def item_exists(data, target):
    return target in set(data)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(f"List: {list1}, Target: {target1}, Exists: {item_exists(list1, target1)}")
    
    list2 = ['a', 'b', 'c']
    target2 = 'd'
    print(f"List: {list2}, Target: {target2}, Exists: {item_exists(list2, target2)}")
    
    list3 = [10, 20, 30]
    target3 = 20
    print(f"List: {list3}, Target: {target3}, Exists: {item_exists(list3, target3)}")
    
    empty_list = []
    target4 = 5
    print(f"List: {empty_list}, Target: {target4}, Exists: {item_exists(empty_list, target4)}")