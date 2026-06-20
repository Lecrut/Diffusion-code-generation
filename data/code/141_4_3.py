def evaluate_booleans(ops, *bools):
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
    A = True
    B = False
    C = True
    result = evaluate_booleans(['NOT', 'AND'], A, B, C)
    print(result)