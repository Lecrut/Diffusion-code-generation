def check_tuple_existence(data_list, target_tuple):
    return target_tuple in data_list

if __name__ == '__main__':
    list1 = [(1, 2), (3, 4), (5, 6)]
    target1 = (3, 4)
    print(f"List: {list1}, Target: {target1} -> Result: {check_tuple_existence(list1, target1)}")
    
    list2 = [(7, 8), (9, 10)]
    target2 = (11, 12)
    print(f"\nList: {list2}, Target: {target2} -> Result: {check_tuple_existence(list2, target2)}")