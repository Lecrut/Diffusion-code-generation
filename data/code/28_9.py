def is_largest_greater(data, target):
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
    print(is_largest_greater(list1, target1))
    list2 = [10, 20, 30, 40]
    target2 = 45
    print(is_largest_greater(list2, target2))
    list3 = [5, 5, 5]
    target3 = 4
    print(is_largest_greater(list3, target3))
    list4 = [-10, -5, -20]
    target4 = -15
    print(is_largest_greater(list4, target4))