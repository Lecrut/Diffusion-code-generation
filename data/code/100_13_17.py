class LogicChecker:

    @staticmethod
    def and_operation(a: bool, b: bool) -> bool:
        return a & b

    @staticmethod
    def or_operation(a: bool, b: bool) -> bool:
        return a | b

    @staticmethod
    def not_operation(a: bool) -> bool:
        return not a

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator == 'and':
            return self.and_operation(a, b)
        elif operator == 'or':
            return self.or_operation(a, b)
        elif operator == 'not':
            if not a and (not b):
                raise ValueError("Both operands are False for 'not' operation")
            return self.not_operation(a or b)
        else:
            raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(False, True, 'or'))
    try:
        print(checker.evaluate(False, False, 'not'))
    except ValueError as e:
        print(e)