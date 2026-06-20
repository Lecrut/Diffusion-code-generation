class LogicChecker:

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            raise ValueError("Unsupported operator for 'not': Both operands are True")
        else:
            raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    try:
        print(checker.evaluate(False, False, 'not'))
    except ValueError as e:
        print(e)