def evaluate_conditions(a, b, c):
    return (a > 0) + (b > 0) + (c > 0) >= 2
if __name__ == '__main__':
    print(evaluate_conditions(1, -2, 3))
    print(evaluate_conditions(-1, -2, -3))
    print(evaluate_conditions(0, 0, 1))