def both_false_generator(a: bool, b: bool):
    if not a and not b:
        yield True

if __name__ == '__main__':
    for result in both_false_generator(False, False):
        print(result)
    for result in both_false_generator(True, False):
        print(result)
    for result in both_false_generator(False, True):
        print(result)
    for result in both_false_generator(True, True):
        print(result)