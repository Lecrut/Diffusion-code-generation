def check_both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    sample_x = False
    sample_y = True
    result = check_both_false(sample_x, sample_y)
    print(result)