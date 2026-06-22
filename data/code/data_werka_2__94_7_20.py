def check_any_truthy(iterable):
    if not hasattr(iterable, '__iter__'):
        raise ValueError("Input must be an iterable")
    for element in iterable:
        if element:
            return True
    return False

if __name__ == '__main__':
    print(check_any_truthy([False, False, True]))
    print(check_any_truthy([False, False, False]))
    print(check_any_truthy([]))
    print(check_any_truthy([0, 0, 0]))
    print(check_any_truthy([None, None, None]))