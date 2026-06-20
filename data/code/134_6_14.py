def is_mutually_exclusive_set(s):
    count_true = sum(1 for value in s if value)
    return count_true == 1

if __name__ == '__main__':
    print(is_mutually_exclusive_set({True, False}))
    print(is_mutually_exclusive_set({False, False}))
    print(is_mutually_exclusive_set({True, True}))
    print(is_mutually_exclusive_set({}))