def evaluate_expressions():
    expressions = [
        5 > 3,
        2 < 4,
        10 == 10,
        8 != 9,
        True and False,
        not True
    ]
    for expr in expressions:
        print(expr)

if __name__ == '__main__':
    evaluate_expressions()