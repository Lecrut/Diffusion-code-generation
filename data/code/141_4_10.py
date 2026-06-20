def combine_booleans(ops, *values):
    result = values[0]
    for op, value in zip(ops, values[1:]):
        if op == 'AND':
            result &= value
        elif op == 'OR':
            result |= value
        elif op == 'NOT':
            result = not result
    return result
if __name__ == '__main__':
    print(combine_booleans(['AND', 'OR'], True, False, True))