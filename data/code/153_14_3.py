def find_target_index(data, target):
    for i, value in enumerate(data):
        if value == target:
            return {"found": True, "index": i}
    return {"found": False}
if __name__ == '__main__':
    list1 = [10, 25, 30, 45, 50]
    target1 = 30
    result1 = find_target_index(list1, target1)
    print(f"List: {list1}, Target: {target1}, Result: {result1}")
    list2 = [1, 5, 9, 12, 15]
    target2 = 10
    result2 = find_target_index(list2, target2)
    print(f"List: {list2}, Target: {target2}, Result: {result2}")
    list3 = [5, 1, 8, 3]
    target3 = 8
    result3 = find_target_index(list3, target3)
    print(f"List: {list3}, Target: {target3}, Result: {result3}")
    list4 = [1, 2, 3]
    target4 = 99
    result4 = find_target_index(list4, target4)
    print(f"List: {list4}, Target: {target4}, Result: {result4}")