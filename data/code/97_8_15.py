def truth_table(a, b):
    return {
        'a': a,
        'b': b,
        'not_a': not a,
        'not_b': not b,
        'and_ab': a and b,
        'or_ab': a or b,
        'xor_ab': a != b
    }

if __name__ == '__main__':
    print(truth_table(True, True))
    print(truth_table(True, False))
    print(truth_table(False, True))
    print(truth_table(False, False))