def check_any_true(boolean_list):
    if not all(isinstance(item, bool) for item in boolean_list):
        raise ValueError("All elements in the list must be boolean values.")
    return any(boolean_list)

if __name__ == '__main__':
    print(check_any_true([False, False, True]))
    print(check_any_true([False, False, False]))