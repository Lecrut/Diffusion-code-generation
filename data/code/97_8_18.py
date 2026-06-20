def truth_table(a, b):
    return {
        'A': a,
        'B': b,
        'AND': a and b,
        'OR': a or b,
        'NOT A': not a,
        'NOT B': not b
    }

if __name__ == '__main__':
    print(truth_table(True, False))