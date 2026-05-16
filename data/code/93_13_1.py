def both_false(a, b):
    return not a and not b
if __name__ == '__main__':
    x = False
    y = False
    result = both_false(x, y)
    print(result)