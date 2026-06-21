def evaluate_expression(expr: str) -> bool:
    return eval(expr)

logical_operators = {
    "AND": lambda x, y: x and y,
    "OR": lambda x, y: x or y,
    "NOT": lambda x: not x
}

def check_pairwise_consistency(pairs):
    for pair in pairs:
        if len(pair) != 2:
            raise ValueError("Each pair must contain exactly two expressions")
        expr1, expr2 = pair
        value1 = evaluate_expression(expr1)
        value2 = evaluate_expression(expr2)
        if logical_operators.get("AND", lambda x, y: False)(value1, value2) or \
           logical_operators.get("OR", lambda x, y: False)(value1, value2):
            return False
    return True

if __name__ == '__main__':
    pairs = [
        ("True and False", "False"),
        ("not A", "A"),
        ("B implies C", "C or not B")
    ]
    print(check_pairwise_consistency(pairs))