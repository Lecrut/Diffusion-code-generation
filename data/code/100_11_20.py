def all_true_or_false(lst):
    if not lst:
        return True
    first = lst[0]
    for item in lst:
        if item != first:
            return False
    return True
if __name__ == '__main__':
    print(all_true_or_false([True, True, True]))
    print(all_true_or_false([False, False, False]))
    print(all_true_or_false([True, False, True]))