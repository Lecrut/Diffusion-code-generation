def evaluate_expression(expr: str) -> bool:
    try:
        return eval(expr)
    except Exception as e:
        raise ValueError(f"Invalid boolean expression: {expr}") from e

def check_pairwise_consistency(pairs):
    logical_operators = {
        "AND": lambda x, y: x and y,
        "OR": lambda x, y: x or y,
        "NOT": lambda x: not x
    }
    for expr1, expr2 in pairs:
        value1 = evaluate_expression(expr1)
        value2 = evaluate_expression(expr2)
        if logical_operators.get("AND", lambda x, y: False)(value1, value2) or \
           logical_operators.get("OR", lambda x, y: False)(value1, value2):
            return False
    return True

if __name__ == '__main__':
    pairs = [
        ("True and False", "False or True"),
        ("A", "not A"),
        ("B and C", "not (B or not C)")
    ]
    print(check_pairwise_consistency(pairs))