def check_existence(data, target):
    for item in data:
        if item == target:
            yield True
            return
    yield False
if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    target1 = 3
    print(f"List: {list1}, Target: {target1} -> ", end="")
    for result in check_existence(list1, target1):
        print(result, end=" ")
    print()
    list2 = [10, 20, 30]
    target2 = 5
    print(f"List: {list2}, Target: {target2} -> ", end="")
    for result in check_existence(list2, target2):
        print(result, end=" ")
    print()
    list3 = [7, 8, 9]
    target3 = 9
    print(f"List: {list3}, Target: {target3} -> ", end="")
    for result in check_existence(list3, target3):
        print(result, end=" ")
    print()