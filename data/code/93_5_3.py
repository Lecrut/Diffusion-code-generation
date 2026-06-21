def check_both_false_gen(a, b):
    if not isinstance(a, bool) or not isinstance(b, bool):
        raise ValueError("Inputs must be boolean values")
    if not a and not b:
        yield True
    else:
        yield False

if __name__ == '__main__':
    result = list(check_both_false_gen(False, False))
    print(result)