class LogicChecker:

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            if a and b:
                raise ValueError("Both operands cannot be True for 'not' operation")
            return not (a or b)
        else:
            raise ValueError("Invalid operator. Use 'and', 'or', or 'not'")
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    try:
        print(checker.evaluate(True, True, 'not'))
    except ValueError as e:
        print(e)