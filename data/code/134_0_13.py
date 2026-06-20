def are_conditions_mutually_exclusive(a: bool, b: bool, c: bool) -> bool:
    return (a ^ b) & (b ^ c) & (c ^ a)
if __name__ == '__main__':
    print(are_conditions_mutually_exclusive(True, False, True))
    print(are_conditions_mutually_exclusive(False, True, False))
    print(are_conditions_mutually_exclusive(True, False, False))