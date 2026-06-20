def are_conditions_mutually_exclusive(a, b, c):
    return bool((a ^ b) & (b ^ c) & (c ^ a))

if __name__ == '__main__':
    print(are_conditions_mutually_exclusive(True, False, True))
    print(are_conditions_mutually_exclusive(False, False, False))
    print(are_conditions_mutually_exclusive(True, True, False))