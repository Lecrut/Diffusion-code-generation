def combine_booleans(ops, *args):
    if ops == 'AND':
        return all(args)
    elif ops == 'OR':
        return any(args)
    elif ops == 'NOT':
        return not args[0]
    else:
        raise ValueError('Invalid operation')
if __name__ == '__main__':
    print(combine_booleans('AND', True, False, True))
    print(combine_booleans('OR', True, False, True))
    print(combine_booleans('NOT', False))