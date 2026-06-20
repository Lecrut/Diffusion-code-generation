def are_strictly_true(a, b):
    return bool(a) and bool(b)

if __name__ == '__main__':
    print(are_strictly_true(True, True))
    print(are_strictly_true(False, True))
    print(are_strictly_true(True, False))
    print(are_strictly_true(False, False))