class LogicChecker:
    OPERAND_MAP = {'and': lambda a, b: a & b, 'or': lambda a, b: a | b}
    NOT_MAP = {'not': lambda a: not a}

    @staticmethod
    def _validate_bool(value, name):
        if not isinstance(value, bool):
            raise ValueError(f"{name} must be a boolean")

    def evaluate(self, operand1, operand2=None, operator='and'):
        self._validate_bool(operand1, 'operand1')
        if operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' expects no second operand")
            return self.NOT_MAP[operator](operand1)
        
        if operand2 is None:
            raise ValueError("Operator requires two operands")
        
        self._validate_bool(operand2, 'operand2')
        
        if operator not in self.OPERAND_MAP:
            raise ValueError(f"Unsupported operator: {operator}")
            
        return self.OPERAND_MAP[operator](operand1, operand2)

if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, True, 'and'))
    print(checker.evaluate(False, True, 'or'))
    print(checker.evaluate(True, operator='not'))
    print(checker.evaluate(False, False, 'and'))
    print(checker.evaluate(True, False, 'or'))