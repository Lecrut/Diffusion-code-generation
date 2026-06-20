def any_true(lst):
    return any(lst)

if __name__ == '__main__':
    print(any_true([True, False, False]))
    print(any_true([False, False, False]))
    print(any_true([]))