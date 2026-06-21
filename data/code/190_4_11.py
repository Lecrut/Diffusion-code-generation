def check_tuple_existence(data, target):
    return target in data

if __name__ == '__main__':
    list1 = (1, 2, 3, 4, 5)
    target1 = 3
    print(f"List: {list1}, Target: {target1} -> Result: {check_tuple_existence(list1, target1)}")
    
    list2 = (10, 20, 30)
    target2 = 5
    print(f"List: {list2}, Target: {target2} -> Result: {check_tuple_existence(list2, target2)}")
    
    list3 = ('a', 'b', 'c')
    target3 = 'd'
    print(f"List: {list3}, Target: {target3} -> Result: {check_tuple_existence(list3, target3)}")