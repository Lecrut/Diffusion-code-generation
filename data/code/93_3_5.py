def both_false(x, y):
    def is_falsy(val):
        return not val
    if not is_falsy(x):
        return False
    if not is_falsy(y):
        return False
    return True

if __name__ == '__main__':
    x = 0
    y = 0
    result = both_false(x, y)
    print(result)