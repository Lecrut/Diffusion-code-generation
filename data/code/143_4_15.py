from sympy import symbols, Eq, solve

def check_contradiction(statement1: str, statement2: str) -> bool:
    x = symbols('x')
    eq1 = Eq(eval(statement1), 0)
    eq2 = Eq(eval(statement2), 0)
    solutions1 = solve(eq1, x)
    solutions2 = solve(eq2, x)
    return not any((sol in solutions2 for sol in solutions1))
if __name__ == '__main__':
    print(check_contradiction('x + 1', 'x - 1'))
    print(check_contradiction('x**2 - 4', 'x - 2'))