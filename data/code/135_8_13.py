from sympy import simplify_logic, to_cnf

class PropositionalLogicEvaluator:
    def to_cnf(self, formula):
        return str(to_cnf(simplify_logic(formula)))

    def compare_cnf(self, cnf1, cnf2):
        return set(cnf1.split('&')) == set(cnf2.split('&'))

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    formula1 = '(A and B) or not C'
    formula2 = 'not C or (A and B)'
    cnf1 = evaluator.to_cnf(formula1)
    cnf2 = evaluator.to_cnf(formula2)
    result = evaluator.compare_cnf(cnf1, cnf2)
    print(result)