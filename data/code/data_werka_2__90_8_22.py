def check_condition(*args):
    return any(args)

if __name__ == '__main__':
    result = check_condition(False, True, False)
    print(result)