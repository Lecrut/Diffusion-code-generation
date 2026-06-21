def check_logical_contradictions(expr1: str, expr2: str) -> bool:
    def evaluate(expression: str) -> bool:
        return eval(expression)

    return evaluate(expr1) != evaluate(expr2)

if __name__ == '__main__':
    print(check_logical_contradictions("True and False", "False or True"))
    print(check_logical_contradictions("not (True and True)", "True"))