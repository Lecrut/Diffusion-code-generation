def both_false(x, y):
    if x:
        return False
    if y:
        return False
    return True

if __name__ == '__main__':
    x = 0
    y = 0
    print(both_false(x, y))