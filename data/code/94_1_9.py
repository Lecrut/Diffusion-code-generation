def check_any_true(iterable):
    if not isinstance(iterable, (list, tuple)):
        raise ValueError("Input must be an iterable of booleans")
    return any(iterable)

if __name__ == '__main__':
    list1 = [False, False, True, False]
    list2 = [False, False, False]
    list3 = [True]
    list4 = []
    try:
        print(f"list1: {check_any_true(list1)}")
        print(f"list2: {check_any_true(list2)}")
        print(f"list3: {check_any_true(list3)}")
        print(f"list4: {check_any_true(list4)}")
        print(f"string: {check_any_true('hello')}")
    except ValueError as e:
        print(e)