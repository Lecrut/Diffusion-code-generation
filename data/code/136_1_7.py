def evaluate_conditions(a, b, c):
    return (a >= 0) & (b < 10) & (c == a + b)

if __name__ == '__main__':
    print(evaluate_conditions(5, 3, 8))
    print(evaluate_conditions(-2, 7, 9))