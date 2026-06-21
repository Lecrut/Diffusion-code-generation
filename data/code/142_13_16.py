def check_equality(expr1: bool, expr2: bool) -> str:
    return "Identical" if expr1 == expr2 else "Different"

if __name__ == '__main__':
    sample_expr1 = (2 < 4) or (3 > 1)
    sample_expr2 = False
    result = check_equality(sample_expr1, sample_expr2)
    print(result)