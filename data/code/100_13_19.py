class LogicChecker:
    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            if a and b:
                raise ValueError("Both operands are True for 'not' operation")
            return not (a or b)
        else:
            raise ValueError(f'Unsupported operator: {operator}')

if __name__ == '__main__':
    checker = LogicChecker()
    result_and = checker.evaluate(True, False, 'and')
    result_or = checker.evaluate(False, True, 'or')
    try:
        result_not = checker.evaluate(True, True, 'not')
    except ValueError as e:
        result_not = str(e)
    
    print(f"Input A: True, Input B: False")
    print(f"AND result: {result_and}")
    print(f"OR result: {result_or}")
    print(f"NOT result: {result_not}")