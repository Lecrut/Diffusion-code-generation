class PropositionalLogicEvaluator:
    def to_cnf(self, formula):
        return formula.replace(' ', '').replace('&', 'AND').replace('|', 'OR')

    def compare_formulas(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return set(cnf1.split()) == set(cnf2.split())

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.compare_formulas('(A & B) | (C & D)', '(D & C) | (B & A)')
    print(result)