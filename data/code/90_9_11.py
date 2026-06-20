def check_condition(*args):
    result = False
    for arg in args:
        if arg:
            result = True
            break
    return result

if __name__ == '__main__':
    sample_values = (False, True, False)
    print(check_condition(*sample_values))