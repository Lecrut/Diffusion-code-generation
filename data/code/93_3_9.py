def check_both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    sample_values = {False: False, True: False}
    result = all(check_both_false(x, y) for x, y in sample_values.items())
    print(result)