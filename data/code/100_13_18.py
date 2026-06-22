class LogicChecker:
    def evaluate(self, operand1: bool, operand2: bool, operator: str) -> bool:
        if operator == 'and':
            return operand1 & operand2
        if operator == 'or':
            return operand1 | operand2
        if operator == 'not':
            if operand2 is None:
                return not operand1
            raise ValueError("Operator 'not' requires one operand.")
        raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, False, 'or'))
    print(checker.evaluate(True, None, 'not'))
    print(checker.evaluate(False, True, 'and'))
    print(checker.evaluate(False, False, 'or'))
    print(checker.evaluate(False, None, 'not'))