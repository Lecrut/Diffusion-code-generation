def find_first_occurrence(data, target):
    for i, element in enumerate(data):
        if element == target:
            return i
    return -1
if __name__ == '__main__':
    list1 = [10, 20, 30, 20, 40]
    target1 = 20
    result1 = find_first_occurrence(list1, target1)
    print(f"List: {list1}, Target: {target1}, Index: {result1}")
    list2 = [5, 15, 25, 35]
    target2 = 10
    result2 = find_first_occurrence(list2, target2)
    print(f"List: {list2}, Target: {target2}, Index: {result2}")
    list3 = [1, 2, 3]
    target3 = 4
    result3 = find_first_occurrence(list3, target3)
    print(f"List: {list3}, Target: {target3}, Index: {result3}")
    list4 = ['a', 'b', 'c']
    target4 = 'c'
    result4 = find_first_occurrence(list4, target4)
    print(f"List: {list4}, Target: {target4}, Index: {result4}")