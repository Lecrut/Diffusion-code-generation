def evaluate_conditions(a, b, c):
    return (a >= 0 and a <= 10) and (b >= 0 and b <= 20) and (c >= 0 and c <= 30)
if __name__ == '__main__':
    print(evaluate_conditions(5, 15, 25))
    print(evaluate_conditions(-1, 15, 25))
    print(evaluate_conditions(5, 30, 25))