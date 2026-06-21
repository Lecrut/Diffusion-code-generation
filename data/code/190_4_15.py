def check_tuple_existence(data, target):
    if not isinstance(data, list) or not all(isinstance(item, tuple) for item in data):
        raise ValueError("Data must be a list of tuples.")
    if not isinstance(target, tuple):
        raise ValueError("Target must be a tuple.")
    
    return target in data

if __name__ == '__main__':
    list1 = [(1, 2), (3, 4), (5, 6)]
    target1 = (3, 4)
    print(f"List: {list1}, Target: {target1} -> Result: {check_tuple_existence(list1, target1)}")
    
    list2 = [(7, 8), (9, 10), (11, 12)]
    target2 = (5, 6)
    print(f"List: {list2}, Target: {target2} -> Result: {check_tuple_existence(list2, target2)}")
    
    list3 = [('a', 'b'), ('c', 'd')]
    target3 = ('e', 'f')
    print(f"List: {list3}, Target: {target3} -> Result: {check_tuple_existence(list3, target3)}")