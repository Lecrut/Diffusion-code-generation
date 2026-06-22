def both_false_gen(a, b):
    if not (a is False and b is False):
        return
    yield True

if __name__ == '__main__':
    result = list(both_false_gen(False, False))
    print(result)