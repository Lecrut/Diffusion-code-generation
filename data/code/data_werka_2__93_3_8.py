def both_false(x, y):
    if not x:
        return not y
    return False

if __name__ == '__main__':
    x = 0
    y = 0
    print(both_false(x, y))