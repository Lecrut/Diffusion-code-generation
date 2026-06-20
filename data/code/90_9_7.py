def check_condition(*args):
    result = False
    for arg in args:
        if arg:
            result = True
            break
    return result
if __name__ == '__main__':
    sample_values1 = (True, False, False)
    print(check_condition(*sample_values1))
    sample_values2 = (False, False, False)
    print(check_condition(*sample_values2))
    sample_values3 = (False, True, False)
    print(check_condition(*sample_values3))