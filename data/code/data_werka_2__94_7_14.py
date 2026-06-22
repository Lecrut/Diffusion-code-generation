def any_truthy(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    result = any_truthy([False, False, True, False])
    print(result)
    result2 = any_truthy([False, False, False])
    print(result2)
    result3 = any_truthy([0, 0, 0, 0])
    print(result3)
    result4 = any_truthy([1, 2, 3])
    print(result4)