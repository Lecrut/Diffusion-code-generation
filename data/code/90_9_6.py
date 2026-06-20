def check_condition(*args):
    return any(args)

if __name__ == '__main__':
    sample_values = (True, False, True)
    result = check_condition(*sample_values)
    print(result)