class LogicChecker:
    def evaluate(self, operand1: bool, operand2: bool, operator: str) -> bool:
        if operator == 'and':
            return bool(operand1 & operand2)
        if operator == 'or':
            return bool(operand1 | operand2)
        if operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' requires only one operand.")
            return not operand1
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, False, 'or'))
    print(checker.evaluate(True, None, 'not'))
    print(checker.evaluate(False, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    print(checker.evaluate(False, None, 'not'))