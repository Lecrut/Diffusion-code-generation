def is_any_true(value, values):
    if value:
        return True
    for v in values:
        if v:
            return True
    return False

if __name__ == '__main__':
    print(is_any_true(False, [False, False, True]))
    print(is_any_true(True, [False, False, False]))
    print(is_any_true(False, [False, False, False]))