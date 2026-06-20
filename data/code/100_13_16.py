class LogicChecker:

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError('Both operands must be boolean values')
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            if operator == 'not' and (a or b):
                raise ValueError("Invalid use of 'not' with non-zero operands")
            return not a
        else:
            raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(False, True, 'or'))
    try:
        print(checker.evaluate(True, True, 'not'))
    except ValueError as e:
        print(e)