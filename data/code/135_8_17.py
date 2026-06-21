from sympy import symbols, And, Or, Not, simplify

class PropositionalLogicEvaluator:
    def __init__(self):
        self.variables = set()

    def to_cnf(self, formula):
        expr = self.parse_formula(formula)
        cnf_expr = simplify(expr)
        return self.extract_clauses(cnf_expr)

    def parse_formula(self, formula):
        symbols_set = set()
        for char in formula:
            if char.isalpha():
                symbols_set.add(char)
        self.variables.update(symbols_set)
        return eval(formula, {'__builtins__': None}, {char: symbols(char) for char in symbols_set})

    def extract_clauses(self, expr):
        clauses = []
        if isinstance(expr, And):
            for subexpr in expr.args:
                clauses.extend(self.extract_clauses(subexpr))
        elif isinstance(expr, Or):
            clauses.append(expr)
        else:
            clauses.append(Or(expr))
        return clauses

    def is_equivalent(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return set(cnf1) == set(cnf2)

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.is_equivalent('(A & B) | C', '(C | A) & (B | C)')
    print(result)