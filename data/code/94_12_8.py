def check_any_true(lst):
    if not all(isinstance(x, bool) for x in lst):
        raise ValueError("All elements in the list must be boolean values.")
    return any(lst)

if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))