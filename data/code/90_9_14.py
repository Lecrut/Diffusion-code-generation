def check_condition(*args):
    if args:
        for arg in args:
            if arg:
                return True
    return False

if __name__ == '__main__':
    sample_values = (False, False, True)
    result = check_condition(*sample_values)
    print(result)