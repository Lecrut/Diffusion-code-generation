def check_both_false(a, b):
    return not a and not b

if __name__ == '__main__':
    a = 0
    b = False
    result = check_both_false(a, b)
    print(result)