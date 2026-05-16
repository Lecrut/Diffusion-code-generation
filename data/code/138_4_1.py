def truth_table(a, b):
    result = [
        (a, b),
        (a, not b),
        (not a, b),
        (not a, not b)
    ]
    return tuple(result)
if __name__ == '__main__':
    print(truth_table(True, True))
    print(truth_table(True, False))
    print(truth_table(False, True))
    print(truth_table(False, False))