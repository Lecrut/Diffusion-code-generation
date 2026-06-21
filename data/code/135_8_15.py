class PropositionalLogicEvaluator:
    def to_cnf(self, formula):
        if 'and' in formula:
            return set(formula.split(' and '))
        elif 'or' in formula:
            return {formula}
        else:
            return {formula}

    def is_equivalent(self, formula1, formula2):
        cnf1 = self.to_cnf(formula1)
        cnf2 = self.to_cnf(formula2)
        return cnf1 == cnf2

if __name__ == '__main__':
    evaluator = PropositionalLogicEvaluator()
    result = evaluator.is_equivalent('A and B', 'B and A')
    print(result)