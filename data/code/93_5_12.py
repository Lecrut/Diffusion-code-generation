def both_false_generator(a: bool, b: bool):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both inputs must be boolean values.")
    if not a and not b:
        yield True

if __name__ == '__main__':
    print(list(both_false_generator(False, False)))
    print(list(both_false_generator(True, False)))
    print(list(both_false_generator(False, True)))
    print(list(both_false_generator(True, True)))