def evaluate_conditions(a, b, c):
    result = (a > 0) and (b < 10) or (c == 5)
    return bool(result)

if __name__ == '__main__':
    x = 5
    y = 8
    z = 5
    print(evaluate_conditions(x, y, z))