def check_any_true(lst):
    if not isinstance(lst, list) or not all(isinstance(x, bool) for x in lst):
        raise ValueError("Input must be a list of boolean values")
    return any(lst)

if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))
    print(check_any_true([]))