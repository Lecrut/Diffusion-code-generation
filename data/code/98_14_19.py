def evaluate_conditions(a, b, c):
    positive_count = sum([a > 0, b > 0, c > 0])
    return positive_count >= 2

if __name__ == '__main__':
    print(evaluate_conditions(1, -1, 3))
    print(evaluate_conditions(-1, -1, 3))
    print(evaluate_conditions(0, 0, 5))