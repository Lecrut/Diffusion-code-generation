def any_true(lst):
    return any(lst)

if __name__ == '__main__':
    print(any_true([False, False, True]))
    print(any_true([]))
    print(any_true([False, False, False]))