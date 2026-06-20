def check_both_false(x, y):
    return not x and not y

if __name__ == '__main__':
    x = True
    y = False
    result = check_both_false(x, y)
    print(result)