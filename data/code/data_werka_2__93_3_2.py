def both_false(x, y):
    values = {True: False, False: True}
    return values[x] and values[y]

if __name__ == '__main__':
    x = 0
    y = 0
    result = both_false(x, y)
    print(result)