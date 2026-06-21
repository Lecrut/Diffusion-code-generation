def check_condition(*args):
    accumulated = False
    for val in args:
        if not accumulated:
            accumulated = val
        else:
            if val:
                break
    return accumulated
if __name__ == '__main__':
    sample_args = (False, False, True, False)
    result = check_condition(*sample_args)
    print(result)