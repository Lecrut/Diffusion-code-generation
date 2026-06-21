def item_exists(data, target):
    if not isinstance(data, list) or not all(isinstance(item, (int, str)) for item in data):
        raise ValueError("Data must be a list of integers or strings.")
    return target in set(data)

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(f"List: {list1}, Target: {target1}, Exists: {item_exists(list1, target1)}")
    
    list2 = ['a', 'b', 'c']
    target2 = 'd'
    try:
        print(f"List: {list2}, Target: {target2}, Exists: {item_exists(list2, target2)}")
    except ValueError as e:
        print(e)
    
    list3 = [10, 20, 30]
    target3 = 20
    print(f"List: {list3}, Target: {target3}, Exists: {item_exists(list3, target3)}")
    
    empty_list = []
    target4 = 5
    try:
        print(f"List: {empty_list}, Target: {target4}, Exists: {item_exists(empty_list, target4)}")
    except ValueError as e:
        print(e)