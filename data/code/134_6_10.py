EXPECTED_TRUE_COUNT = 1

def is_mutually_exclusive_set(s):
    return sum(s) == EXPECTED_TRUE_COUNT
if __name__ == '__main__':
    print(is_mutually_exclusive_set({True, False}))
    print(is_mutually_exclusive_set({False, False}))
    print(is_mutually_exclusive_set({True, True}))
    print(is_mutually_exclusive_set({}))