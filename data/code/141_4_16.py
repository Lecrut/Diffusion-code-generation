def combine_booleans(ops, *bools):
    if len(bools) != len(ops) + 1:
        raise ValueError('Mismatch between number of operations and boolean values')
    result = bools[0]
    for op, b in zip(ops, bools[1:]):
        if op == 'AND':
            result &= b
        elif op == 'OR':
            result |= b
        elif op == 'NOT':
            result = not b
        else:
            raise ValueError('Invalid operator')
    return result
if __name__ == '__main__':
    print(combine_booleans(['AND', 'OR'], True, False, True))