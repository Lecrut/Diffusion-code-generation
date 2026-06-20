def combine_booleans(*args, operator):
    if operator == 'AND':
        return all(args)
    elif operator == 'OR':
        return any(args)
    elif operator == 'NOT':
        return not args[0]
    else:
        raise ValueError('Invalid operator')
if __name__ == '__main__':
    print(combine_booleans(True, False, True, operator='AND'))
    print(combine_booleans(True, False, True, operator='OR'))
    print(combine_booleans(False, operator='NOT'))