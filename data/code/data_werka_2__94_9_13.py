def check_any_true(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    print(check_any_true([False, False, True, False]))
    print(check_any_true([False, False, False]))
    print(check_any_true([]))
    print(check_any_true([True, True, True]))