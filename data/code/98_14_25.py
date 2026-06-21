def evaluate_conditions(a, b, c):
    result = (a > 0) and (b < 10) or (c == 5)
    return bool(result)

if __name__ == '__main__':
    print(evaluate_conditions(1, 5, 5))
    print(evaluate_conditions(-1, 11, 6))
    print(evaluate_conditions(0, 5, 5))