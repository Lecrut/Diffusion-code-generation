def check_any_true(iterable):
    for value in iterable:
        if value:
            return True
    return False
if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))