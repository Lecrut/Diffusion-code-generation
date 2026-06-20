def are_conditions_mutually_exclusive(a: bool, b: bool, c: bool) -> bool:
    return (a ^ b) and ((not a) or (not b)) and (b ^ c) and ((not b) or (not c)) and (c ^ a) and ((not c) or (not a))

if __name__ == '__main__':
    print(are_conditions_mutually_exclusive(True, False, False))
    print(are_conditions_mutually_exclusive(False, True, False))
    print(are_conditions_mutually_exclusive(False, False, True))
    print(are_conditions_mutually_exclusive(True, True, False))
    print(are_conditions_mutually_exclusive(False, True, True))
    print(are_conditions_mutually_exclusive(True, False, True))
    print(are_conditions_mutually_exclusive(True, True, True))