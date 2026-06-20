class PropositionalLogicEvaluator:
    def __init__(self):
        self.parentheses_stack = []

    def to_cnf(self, formula):
        formula = formula.replace(' ', '')
        formula = formula.replace('and', '&')
        formula = formula.replace('or', '|')
        return formula

    def compare_cnf(self, cnf1, cnf2):
        cnf1_clauses = set(cnf1.split('&'))
        cnf2_clauses = set(cnf2.split('&'))
        return cnf1_clauses == cnf2_clauses

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    formula1 = 'A and B or C'
    formula2 = '(A and B) or C'
    cnf1 = evaluator.to_cnf(formula1)
    cnf2 = evaluator.to_cnf(formula2)
    result = evaluator.compare_cnf(cnf1, cnf2)
    print(result)