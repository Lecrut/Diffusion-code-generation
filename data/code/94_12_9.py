def check_any_true(lst):
    return any(lst)

if __name__ == '__main__':
    list1 = [False, False, True]
    list2 = [False, False, False]
    print(f"List 1: {list1}, Result: {check_any_true(list1)}")
    print(f"List 2: {list2}, Result: {check_any_true(list2)}")