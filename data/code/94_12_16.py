def check_any_true(lst):
    return any(lst)

if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))
    print(check_any_true([True, False, False]))
    print(check_any_true([]))
    print(check_any_true([False]))