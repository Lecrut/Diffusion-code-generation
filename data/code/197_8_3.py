def contains_target(iterable, target):
    return any(item == target for item in iterable)
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    target1 = 8
    result1 = contains_target(list1, target1)
    print(f"List: {list1}, Target: {target1}, Contains: {result1}")
    list2 = [10, 20, 30, 40]
    target2 = 5
    result2 = contains_target(list2, target2)
    print(f"List: {list2}, Target: {target2}, Contains: {result2}")
    list3 = ['a', 'b', 'c']
    target3 = 'd'
    result3 = contains_target(list3, target3)
    print(f"List: {list3}, Target: {target3}, Contains: {result3}")
    list4 = [1, 2, 3]
    target4 = 2
    result4 = contains_target(list4, target4)
    print(f"List: {list4}, Target: {target4}, Contains: {result4}")