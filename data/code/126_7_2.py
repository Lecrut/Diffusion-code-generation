def check_all_equal(items):
    if not items:
        return True
    first_element = items[0]
    for item in items:
        if item != first_element:
            return False
    return True
if __name__ == '__main__':
    list1 = [1, 1, 1]
    list2 = [5, 5, 5]
    list3 = [1, 2, 1]
    list4 = []
    list5 = [10]
    print(f"list1: {check_all_equal(list1)}")
    print(f"list2: {check_all_equal(list2)}")
    print(f"list3: {check_all_equal(list3)}")
    print(f"list4: {check_all_equal(list4)}")
    print(f"list5: {check_all_equal(list5)}")