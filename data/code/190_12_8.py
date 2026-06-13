def exists_element_set(target_element, input_list):
    input_set = set(input_list)
    return target_element in input_set
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    target1 = 8
    result1 = exists_element_set(target1, list1)
    print(f"List: {list1}, Target: {target1}, Exists: {result1}")
    list2 = [10, 20, 30, 40]
    target2 = 5
    result2 = exists_element_set(target2, list2)
    print(f"List: {list2}, Target: {target2}, Exists: {result2}")
    list3 = ['a', 'b', 'c']
    target3 = 'd'
    result3 = exists_element_set(target3, list3)
    print(f"List: {list3}, Target: {target3}, Exists: {result3}")
    list4 = [1, 2, 3]
    target4 = 1
    result4 = exists_element_set(target4, list4)
    print(f"List: {list4}, Target: {target4}, Exists: {result4}")