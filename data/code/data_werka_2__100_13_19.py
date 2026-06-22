class LogicChecker:
    OPERATORS = {'and', 'or', 'not'}
    
    def evaluate(self, operand1, operand2=None, operator='and'):
        if operator not in self.OPERATORS:
            raise ValueError(f"Unsupported operator: {operator}")
        
        if operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' takes exactly one operand")
            if not isinstance(operand1, bool):
                raise ValueError("Operands must be boolean values")
            return not operand1
        
        if operand2 is None:
            raise ValueError("Binary operators require two operands")
        if not isinstance(operand1, bool) or not isinstance(operand2, bool):
            raise ValueError("Operands must be boolean values")
            
        if operator == 'and':
            return operand1 & operand2
        elif operator == 'or':
            return operand1 | operand2
        return False

if __name__ == '__main__':
    checker = LogicChecker()
    and_result = checker.evaluate(True, False, 'and')
    or_result = checker.evaluate(True, False, 'or')
    not_result = checker.evaluate(False, operator='not')
    print(and_result)
    print(or_result)
    print(not_result)