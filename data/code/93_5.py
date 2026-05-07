def both_false_generator(a, b):
    if not a and not b:
        yield True
if __name__ == '__main__':
    print(list(both_false_generator(False, False)))
    print(list(both_false_generator(True, False)))
    print(list(both_false_generator(False, True)))
    print(list(both_false_generator(True, True)))