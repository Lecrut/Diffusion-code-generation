def any_true(iterable):
    for value in iterable:
        if value:
            return True
    return False

if __name__ == '__main__':
    result = any_true([False, False, True, False])
    print(result)
    result2 = any_true([False, False, False])
    print(result2)
    result3 = any_true([])
    print(result3)