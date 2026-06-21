class ContradictionEvaluator:

    def __init__(self):
        self.statements = []

    def add_statement(self, statement):
        self.statements.append(statement.lower())

    def check_contradictions(self):
        contradictions = []
        n = len(self.statements)
        for i in range(n):
            for j in range(i + 1, n):
                if self._are_contradictory(self.statements[i], self.statements[j]):
                    contradictions.append((self.statements[i], self.statements[j]))
        return contradictions

    def _are_contradictory(self, s1, s2):
        s1_parts = set(s1.split(';'))
        s2_parts = set(s2.split(';'))
        return bool(s1_parts.intersection(s2_parts)) and all(('not ' + part not in s1_parts for part in s2_parts)) and all(('not ' + part not in s2_parts for part in s1_parts))
if __name__ == '__main__':
    evaluator = ContradictionEvaluator()
    evaluator.add_statement('A; B')
    evaluator.add_statement('not A; C')
    contradictions = evaluator.check_contradictions()
    print(contradictions)