class StatementEvaluator:

    def __init__(self):
        self.statements = {'True': True, 'False': False}

    def evaluate(self, statement):
        return self.statements.get(statement, None)
if __name__ == '__main__':
    evaluator = StatementEvaluator()
    print(evaluator.evaluate('True'))
    print(evaluator.evaluate('False'))
    print(evaluator.evaluate('2 + 2 == 4'))