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
    sample_values = truth_table(True, False)
    print(sample_values)