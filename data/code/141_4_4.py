def combine_booleans(*args):
    if not args:
        return False
    result = args[0]
    for arg in args[1:]:
        if isinstance(result, bool) and isinstance(arg, bool):
            if result == True and arg == True:
                result = True
            elif result == False and arg == False:
                result = False
            else:
                result = True
        else:
            raise ValueError('All arguments must be boolean values')
    return result
if __name__ == '__main__':
    print(combine_booleans(True, True))
    print(combine_booleans(False, False))
    print(combine_booleans(True, False))
    print(combine_booleans(False, True))