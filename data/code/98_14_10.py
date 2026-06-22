def evaluate_conditions(a, b, c, d):
    result = (a > 0) and (b < 10) or (c == d)
    return bool(result)

if __name__ == '__main__':
    x = 5
    y = 8
    z = 10
    w = 10
    print(evaluate_conditions(x, y, z, w))