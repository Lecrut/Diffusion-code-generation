class LogicChecker:
    OPERATORS = {'and', 'or', 'not'}

    @staticmethod
    def _validate_bool(value, name):
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a boolean")

    def evaluate(self, operand1, operand2=None, operator='and'):
        self._validate_bool(operand1, "operand1")
        if operator not in self.OPERATORS:
            raise ValueError(f"Unsupported operator: {operator}")
        
        if operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' requires only one operand")
            return not operand1
        
        self._validate_bool(operand2, "operand2")
        
        if operator == 'and':
            return operand1 & operand2
        if operator == 'or':
            return operand1 | operand2
        return False

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, True, 'and'))
    print(checker.evaluate(False, True, 'or'))
    print(checker.evaluate(True, operator='not'))
    print(checker.evaluate(False, False, 'and'))
    print(checker.evaluate(True, False, 'or'))
    print(checker.evaluate(False, operator='not'))