def is_largest_greater_than(data, target):
    if not data:
        return False
    largest = data[0]
    for x in data[1:]:
        if x > largest:
            largest = x
    return largest > target
if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    target1 = 7
    print(is_largest_greater_than(list1, target1))
    list2 = [10, 2, 5, 1]
    target2 = 9
    print(is_largest_greater_than(list2, target2))
    list3 = [4, 4, 4, 4]
    target3 = 4
    print(is_largest_greater_than(list3, target3))
    list4 = [1, 2, 3]
    target4 = 5
    print(is_largest_greater_than(list4, target4))
    list5 = []
    target5 = 0
    print(is_largest_greater_than(list5, target5))