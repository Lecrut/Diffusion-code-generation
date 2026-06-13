def check_list(data, target):
    for item in data:
        if item == target:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(list1, target1)
    for result in check_list(list1, target1):
        print(result)
    list2 = [10, 20, 30]
    target2 = 5
    print(list2, target2)
    for result in check_list(list2, target2):
        print(result)
    list3 = [5, 6, 7]
    target3 = 10
    print(list3, target3)
    for result in check_list(list3, target3):
        print(result)