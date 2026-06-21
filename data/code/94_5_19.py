def any_true(seq):
    for val in seq:
        if val:
            return True
    return False

if __name__ == '__main__':
    result = any_true([False, False, True, False])
    print(result)