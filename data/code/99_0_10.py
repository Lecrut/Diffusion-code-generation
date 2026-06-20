def evaluate_expression(expression):
    return eval(expression)

if __name__ == '__main__':
    print(evaluate_expression("3 + 5 * (2 - 8)"))