def both_false_generator(a: bool, b: bool):
    if not a and not b:
        yield True

if __name__ == '__main__':
    gen = both_false_generator(False, False)
    print(next(gen))
    gen = both_false_generator(True, True)
    try:
        print(next(gen))
    except StopIteration:
        print(None)