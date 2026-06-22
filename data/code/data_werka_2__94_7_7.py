def any_truthy(iterable):
    for item in iterable:
        if item:
            return True
    return False

if __name__ == '__main__':
    result = any_truthy([False, False, True, False])
    print(result)