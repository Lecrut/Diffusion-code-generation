def both_false_generator(a, b):
    if not (isinstance(a, bool) and isinstance(b, bool)):
        raise ValueError("Inputs must be boolean values")
    yield a is False and b is False

if __name__ == '__main__':
    result = list(both_false_generator(False, False))
    print(result)