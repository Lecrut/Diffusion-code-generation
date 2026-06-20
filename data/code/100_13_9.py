class LogicChecker:

    def validate_operator(self, operator):
        if operator not in ['and', 'or', 'not']:
            raise ValueError(f'Unsupported operator: {operator}')

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        self.validate_operator(operator)
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            return not a
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    print(checker.evaluate(False, False, 'not'))