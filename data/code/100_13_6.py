class LogicChecker:
    SUPPORTED_OPERATORS = ('and', 'or', 'not')

    def __init__(self):
        self._cache = {}

    def evaluate(self, operand1, operand2=None, operator='and'):
        self._validate_operands(operand1, operand2)
        self._validate_operator(operator)
        
        cache_key = (operand1, operand2, operator)
        if cache_key in self._cache:
            return self._cache[cache_key]
        
        result = self._compute(operand1, operand2, operator)
        self._cache[cache_key] = result
        return result

    def _validate_operands(self, operand1, operand2):
        if not isinstance(operand1, bool):
            raise ValueError("First operand must be a boolean")
        
        if operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' should not have a second operand")
        else:
            if operand2 is None:
                raise ValueError("Second operand is required for binary operators")
            if not isinstance(operand2, bool):
                raise ValueError("Second operand must be a boolean")

    def _validate_operator(self, operator):
        if operator not in self.SUPPORTED_OPERATORS:
            raise ValueError(f"Unsupported operator: {operator}")

    def _compute(self, operand1, operand2, operator):
        if operator == 'and':
            return operand1 & operand2
        elif operator == 'or':
            return operand1 | operand2
        elif operator == 'not':
            return not operand1
        return False

if __name__ == '__main__':
    checker = LogicChecker()
    result_and = checker.evaluate(True, True, 'and')
    print(result_and)
    result_or = checker.evaluate(False, True, 'or')
    print(result_or)
    result_not = checker.evaluate(True, None, 'not')
    print(result_not)