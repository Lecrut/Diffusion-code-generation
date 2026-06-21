def validate_inputs(expr1: bool, expr2: bool) -> None:
    if not isinstance(expr1, bool) or not isinstance(expr2, bool):
        raise ValueError("Both inputs must be boolean values")

def compare_booleans(expr1: bool, expr2: bool) -> str:
    validate_inputs(expr1, expr2)
    return "Identical" if expr1 == expr2 else "Different"

if __name__ == '__main__':
    expr1 = (5 > 3) and (10 == 10)
    expr2 = True
    print(compare_booleans(expr1, expr2))