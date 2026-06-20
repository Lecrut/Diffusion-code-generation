def both_false_generator(a, b):
    if not a and not b:
        yield True

if __name__ == '__main__':
    print(next(both_false_generator(False, False)))
    print(next(both_false_generator(True, False)))
    print(next(both_false_generator(False, True)))
    print(next(both_false_generator(True, True)))