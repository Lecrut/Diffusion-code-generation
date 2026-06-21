def check_logical_contradictions(expr1: str, expr2: str) -> bool:

    def evaluate_expression(expr: str) -> bool:
        return eval(expr)
    return evaluate_expression(expr1) != evaluate_expression(expr2)
if __name__ == '__main__':
    print(check_logical_contradictions('True', 'False'))
    print(check_logical_contradictions('(True and False)', '(not True)'))