def both_false_generator(a: bool, b: bool):
    if not a and not b:
        yield True

if __name__ == '__main__':
    result = list(both_false_generator(False, False))
    print(result)
    result = list(both_false_generator(True, False))
    print(result)
    result = list(both_false_generator(False, True))
    print(result)
    result = list(both_false_generator(True, True))
    print(result)