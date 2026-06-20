def both_false_generator(a: bool, b: bool):
    if not a and not b:
        yield True

if __name__ == '__main__':
    gen = both_false_generator(False, False)
    result1 = next(gen)
    print(result1)

    gen = both_false_generator(True, True)
    try:
        result2 = next(gen)
    except StopIteration:
        result2 = None
    print(result2)