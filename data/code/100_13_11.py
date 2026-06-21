class LogicChecker:
    OPERATIONS = {
        'and': lambda a, b: int(a) & int(b),
        'or': lambda a, b: int(a) | int(b),
        'xor': lambda a, b: int(a) ^ int(b),
        'not': lambda a, _: int(not a),
    }

    def __init__(self):
        self._valid_operators = frozenset(self.OPERATIONS.keys())

    def _validate_operands(self, operand1, operand2):
        if not isinstance(operand1, bool):
            raise TypeError("First operand must be a boolean")
        if operand2 is not None and not isinstance(operand2, bool):
            raise TypeError("Second operand must be a boolean")

    def evaluate(self, operand1, operand2=None, operator='and'):
        if not isinstance(operator, str):
            raise TypeError("Operator must be a string")
        
        normalized_operator = operator.strip().lower()
        
        if normalized_operator not in self._valid_operators:
            raise ValueError(f"Unsupported operator: {operator}")
        
        if normalized_operator == 'not':
            self._validate_operands(operand1, None)
            func = self.OPERATIONS['not']
            result_int = func(operand1, None)
            return bool(result_int)
        
        self._validate_operands(operand1, operand2)
        
        if operand2 is None:
            raise ValueError("Operator 'not' requires only one operand, 'and' and 'or' require two")
        
        func = self.OPERATIONS[normalized_operator]
        result_int = func(operand1, operand2)
        return bool(result_int)

if __name__ == '__main__':
    checker = LogicChecker()
    and_result = checker.evaluate(True, False, 'and')
    or_result = checker.evaluate(True, False, 'or')
    not_result = checker.evaluate(True, None, 'not')
    xor_result = checker.evaluate(True, True, 'xor')
    print(and_result)
    print(or_result)
    print(not_result)
    print(xor_result)