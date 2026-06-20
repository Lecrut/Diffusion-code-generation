class PropositionalLogicEvaluator:

    def to_cnf(self, formula):
        formula = formula.lower().replace(' ', '')
        formula = formula.replace('&', 'and').replace('|', 'or')
        return formula

    def compare_formulas(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return set(cnf1.split()) == set(cnf2.split())
if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.compare_formulas('(A & B) | C', '(C | A) & (B | A)')
    print(result)