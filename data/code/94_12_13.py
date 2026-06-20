def check_any_true(lst):
    if not all((isinstance(x, bool) for x in lst)):
        raise ValueError('All elements must be boolean values')
    return any(lst)
if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))
    print(check_any_true([]))
    try:
        print(check_any_true(['True', 'False']))
    except ValueError as e:
        print(e)