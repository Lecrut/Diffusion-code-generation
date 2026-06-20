def combine_booleans(*args):
    if not args:
        return False
    result = args[0]
    for arg in args[1:]:
        if isinstance(result, bool) and isinstance(arg, bool):
            if result == 'and':
                result &= arg
            elif result == 'or':
                result |= arg
            elif result == 'not':
                result = not arg
        else:
            raise ValueError("All arguments must be boolean or a logical operator ('and', 'or', 'not')")
    return result
if __name__ == '__main__':
    print(combine_booleans(True, 'and', False))
    print(combine_booleans(False, 'or', True))
    print(combine_booleans('not', True))