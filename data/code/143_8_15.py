def check_logical_contradictions(expr1: str, expr2: str) -> bool:

    def eval_expr(expression: str) -> bool:
        return eval(expression)
    return eval_expr(expr1) != eval_expr(expr2)
if __name__ == '__main__':
    print(check_logical_contradictions('True', 'False'))
    print(check_logical_contradictions('not False', 'True'))