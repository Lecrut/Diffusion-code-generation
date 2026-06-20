def is_positive(num):
    return num > 0

def evaluate_conditions(a, b, c):
    positives = sum((is_positive(x) for x in [a, b, c]))
    return positives >= 2
if __name__ == '__main__':
    print(evaluate_conditions(1, -2, 3))
    print(evaluate_conditions(-1, -2, -3))
    print(evaluate_conditions(0, 0, 1))