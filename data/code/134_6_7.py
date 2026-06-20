def is_mutually_exclusive_set(s):
    true_count = 0
    for value in s:
        if value:
            true_count += 1
            if true_count > 1:
                return False
    return true_count == 1

if __name__ == '__main__':
    print(is_mutually_exclusive_set({True, False}))
    print(is_mutually_exclusive_set({False, False}))
    print(is_mutually_exclusive_set({True, True}))
    print(is_mutually_exclusive_set({}))