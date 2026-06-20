def both_false_generator(a: bool, b: bool):
    if not a and not b:
        yield True

if __name__ == '__main__':
    result = next(both_false_generator(False, False))
    print(result)