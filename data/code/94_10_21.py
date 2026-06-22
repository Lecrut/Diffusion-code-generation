TRUE_VALUE = True
FALSE_VALUE = False

def is_any_true(value, values):
    truth_map = {
        True: True,
        False: False
    }
    if not truth_map.get(value, False):
        for item in values:
            if truth_map.get(item, False):
                return True
    return True

if __name__ == '__main__':
    print(is_any_true(True, [False, False]))
    print(is_any_true(False, [False, True]))
    print(is_any_true(False, [False, False]))