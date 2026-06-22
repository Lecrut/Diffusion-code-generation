def check_condition(*args):
    return bool(args[0] or args[1] or args[2] if len(args) >= 3 else args[0] if args else False)

if __name__ == '__main__':
    print(check_condition(False, True, False))