OPERANDS = {
    'AND': lambda a, b: a and b,
    'OR': lambda a, b: a or b,
    'NOT': lambda a: not a
}

def combine_booleans(ops, *bools):
    result = bools[0]
    for op in ops:
        result = OPERANDS[op](result, bools[len(ops):][0])
    return result

if __name__ == '__main__':
    A = True
    B = False
    C = True
    result = combine_booleans(['NOT', 'AND'], A, B, C)
    print(result)