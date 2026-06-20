def combine_booleans(ops, *args):
    result = args[0]
    for op, arg in zip(ops, args[1:]):
        if op == 'AND':
            result &= arg
        elif op == 'OR':
            result |= arg
        elif op == 'NOT':
            result = not arg
    return result
if __name__ == '__main__':
    print(combine_booleans(['AND', 'OR'], True, False, True))