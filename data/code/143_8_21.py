def evaluate_expression(expr: str) -> bool:
    return eval(expr)

def check_pairwise_consistency(pairs):
    for expr1, expr2 in pairs:
        value1 = evaluate_expression(expr1)
        value2 = evaluate_expression(expr2)
        if not (value1 == value2 or (not value1 and not value2)):
            return False
    return True

if __name__ == '__main__':
    pairs = [
        ("True", "False"),
        ("A", "not A"),
        ("B and C", "not (B or C)"),
        ("A and B", "B and A")
    ]
    print(check_pairwise_consistency(pairs))