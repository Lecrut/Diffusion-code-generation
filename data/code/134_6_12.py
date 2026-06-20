def is_mutually_exclusive_set(boolean_set):
    return sum(boolean_set) == 1

if __name__ == '__main__':
    print(is_mutually_exclusive_set({True, False}))
    print(is_mutually_exclusive_set({False, False}))
    print(is_mutually_exclusive_set({True, True}))