class LogicChecker:
    AND = 'and'
    OR = 'or'
    NOT = 'not'

    @staticmethod
    def evaluate(a: bool, b: bool, operator: str) -> bool:
        if operator == LogicChecker.AND:
            return a & b
        elif operator == LogicChecker.OR:
            return a | b
        elif operator == LogicChecker.NOT:
            if a and b:
                raise ValueError("Both operands are True for 'not' operation")
            return not (a or b)
        else:
            raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, LogicChecker.AND))
    print(checker.evaluate(True, True, LogicChecker.OR))
    try:
        print(checker.evaluate(True, True, LogicChecker.NOT))
    except ValueError as e:
        print(e)