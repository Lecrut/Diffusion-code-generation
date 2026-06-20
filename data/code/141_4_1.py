def combine_booleans(ops, *bools):
    result = bools[0]
    for op, b in zip(ops, bools[1:]):
        if op == 'AND':
            result &= b
        elif op == 'OR':
            result |= b
        elif op == 'NOT':
            result = not b
    return result
if __name__ == '__main__':
    print(combine_booleans(['AND', 'OR'], True, False, True))