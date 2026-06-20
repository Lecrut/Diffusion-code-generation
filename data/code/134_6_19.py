def is_mutually_exclusive_set(s):
    if not isinstance(s, set) or any(not isinstance(x, bool) for x in s):
        raise ValueError("Input must be a set of boolean values")
    return sum(s) == 1

if __name__ == '__main__':
    print(is_mutually_exclusive_set({True, False}))
    print(is_mutually_exclusive_set({False, False}))
    print(is_mutually_exclusive_set({True, True}))
    print(is_mutually_exclusive_set({}))