class LogicChecker:
    OPERATORS = {'and': lambda a, b: a & b, 'or': lambda a, b: a | b, 'not': lambda a, _: not a}

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator in self.OPERATORS:
            return self.OPERATORS[operator](a, b)
        raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    try:
        print(checker.evaluate(True, True, 'not'))
    except ValueError as e:
        print(e)