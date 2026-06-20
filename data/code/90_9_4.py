def check_condition(*args):
    if args:
        return any(args)
    return False

if __name__ == '__main__':
    sample_values = (True, False, True)
    result = check_condition(*sample_values)
    print(result)