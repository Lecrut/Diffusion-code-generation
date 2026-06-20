def evaluate_conditions(a, b, c):
    return (a >= 0 and a <= 10) and (b >= 5 and b <= 15) and (c >= 10 and c <= 20)
if __name__ == '__main__':
    print(evaluate_conditions(3, 10, 15))
    print(evaluate_conditions(-1, 10, 15))
    print(evaluate_conditions(3, 20, 15))