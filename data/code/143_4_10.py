import sympy as sp

def check_contradiction(statement1: str, statement2: str) -> bool:
    symbols = set(sp.symbols(statement1 + statement2))
    expr1 = sp.sympify(statement1)
    expr2 = sp.sympify(statement2)
    contradiction = sp.satisfiable(expr1 & ~expr2, all_models=True)
    return not any(contradiction)
if __name__ == '__main__':
    print(check_contradiction('x > 0', 'x <= 0'))
    print(check_contradiction('x > 0', 'x >= 1'))