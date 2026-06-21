import sympy as sp

def check_contradictions(statement1: str, statement2: str) -> bool:
    symbols = set(sp.symbols(statement1 + statement2))
    expr1 = sp.sympify(statement1)
    expr2 = sp.sympify(statement2)
    return not sp.satisfiable(expr1 & ~expr2)
if __name__ == '__main__':
    print(check_contradictions('x > 0', 'x <= 0'))
    print(check_contradictions('x > 0', 'x > 1'))