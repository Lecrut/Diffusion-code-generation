def validate_bools(a, b):
    if type(a) is not bool or type(b) is not bool:
        raise ValueError("Both inputs must be boolean types")
    return

def both_false_generator(a, b):
    validate_bools(a, b)
    condition = a is False and b is False
    yield condition

if __name__ == '__main__':
    print(list(both_false_generator(False, False)))
    print(list(both_false_generator(True, False)))
    print(list(both_false_generator(False, True)))
    print(list(both_false_generator(True, True)))