class PropositionalLogicEvaluator:
    def __init__(self):
        self.operators = {'&': 'AND', '|': 'OR', '!': 'NOT'}

    def to_cnf(self, formula):
        import re
        formula = formula.replace(' ', '').replace('(', '').replace(')', '')
        for op in sorted(self.operators.keys(), key=len, reverse=True):
            formula = re.sub(r'\b' + op + r'\b', self.operators[op], formula)
        return formula

    def compare_formulas(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return set(cnf1.split()) == set(cnf2.split())

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.compare_formulas('(A & B) | C', '(C | A) & (B | A)')
    print(result)