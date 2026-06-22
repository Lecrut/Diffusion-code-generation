def check_both_false(a, b):
    return not any([a, b])
if __name__ == '__main__':
    a = 0
    b = None
    result = check_both_false(a, b)
    print(result)