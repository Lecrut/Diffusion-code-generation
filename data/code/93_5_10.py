def both_false_generator(a: bool, b: bool):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Both arguments must be boolean values.")
    if not a and not b:
        yield True

if __name__ == '__main__':
    gen = both_false_generator(False, False)
    print(next(gen))
    gen = both_false_generator(True, False)
    try:
        print(next(gen))
    except StopIteration:
        print("No value to yield")