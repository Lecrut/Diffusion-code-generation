def both_false_generator(a, b):
    if not a and not b:
        yield True

if __name__ == '__main__':
    gen = both_false_generator(False, False)
    result = next(gen)
    print(result)

    gen = both_false_generator(True, True)
    try:
        result = next(gen)
        print(result)
    except StopIteration:
        print("No value generated")