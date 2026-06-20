def fast_bool_compare(a, b):
    return a == b

if __name__ == '__main__':
    print(fast_bool_compare(True, True))
    print(fast_bool_compare(False, False))
    print(fast_bool_compare(True, False))
    print(fast_bool_compare(False, True))