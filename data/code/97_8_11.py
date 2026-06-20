def truth_table(a: bool, b: bool) -> dict:
    return {
        'A': a,
        'B': b,
        'AND': a and b,
        'OR': a or b,
        'NOT A': not a,
        'NOT B': not b
    }

if __name__ == '__main__':
    print(truth_table(True, True))
    print(truth_table(True, False))
    print(truth_table(False, True))
    print(truth_table(False, False))