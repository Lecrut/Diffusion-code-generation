def evaluate_expression(expression):
    if len(expression) == 1:
        return expression[0]
    else:
        left = evaluate_expression(expression[0])
        right = evaluate_expression(expression[1])
        op = expression[2]
        return eval(f"{left} {op} {right}")
if __name__ == '__main__':
    expression = [
        'A',
        'op',
        ['A', 'B'],
        'op',
        'C'
    ]
    expr1 = [True, False, 'and']
    expr2 = [expr1[0], True, 'and']
    final_expression = [expr2[0], False, 'and']
    def recursive_eval(expr):
        if len(expr) == 3:
            left, right, op = expr
            if op == 'and':
                return left and right
            elif op == 'or':
                return left or right
            elif op == 'not':
                return not left
            else:
                raise ValueError(f"Unknown operator: {op}")
        else:
            raise ValueError("Invalid expression structure for this recursive implementation.")
    expr_ab = [True, False, 'and']
    expr_abc = [expr_ab[0], True, 'and']
    final_expr = [expr_abc[0], False, 'and']
    result = recursive_eval(final_expr)
    print(result)