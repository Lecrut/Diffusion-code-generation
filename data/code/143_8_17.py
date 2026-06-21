LOGICAL_OPERATORS = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "NOT": lambda x: not x
}

def evaluate_expression(expr: str) -> bool:
    return eval(expr)

def check_pairwise_consistency(pairs):
    for expr1, expr2 in pairs:
        value1 = evaluate_expression(expr1)
        value2 = evaluate_expression(expr2)
        if LOGICAL_OPERATORS.get("AND", lambda x, y: False)(value1, value2) or \
           LOGICAL_OPERATORS.get("OR", lambda x, y: False)(value1, value2):
            return False
    return True

if __name__ == '__main__':
    pairs = [
        ("True and False", "False"),
        ("not True", "False"),
        ("True or False", "True")
    ]
    print(check_pairwise_consistency(pairs))