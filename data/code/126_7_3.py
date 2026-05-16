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
    list4 = [10]
    list5 = []
    list6 = [3.14, 3.14]
    list7 = [1, 2]
    print(f"list1: {check_all_equal(list1)}")
    print(f"list2: {check_all_equal(list2)}")
    print(f"list3: {check_all_equal(list3)}")
    print(f"list4: {check_all_equal(list4)}")
    print(f"list5: {check_all_equal(list5)}")
    print(f"list6: {check_all_equal(list6)}")
    print(f"list7: {check_all_equal(list7)}")