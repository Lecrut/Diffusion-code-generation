def check_condition(*args):
    status_map = {True: True, False: False}
    return any(status_map.get(val, False) for val in args)

if __name__ == '__main__':
    result = check_condition(False, False, True, False)
    print(result)