def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    list1 = [False, False, True]
    list2 = [False, False, False]
    print(f"list1: {check_any_true(list1)}")
    print(f"list2: {check_any_true(list2)}")