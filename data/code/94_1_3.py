def check_any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true((False, False, False)))