BOOL_TRUE = 1
BOOL_FALSE = 0
UNARY_OPERATOR = 'not'
BINARY_OPERATORS = ('and', 'or')
OPERAND_COUNT_BINARY = 2
OPERAND_COUNT_UNARY = 1

class LogicChecker:
    def evaluate(self, operand1, operand2=None, operator='and'):
        if operator == UNARY_OPERATOR:
            self._validate_single_bool(operand1)
            return self._apply_unary(operand1)
        
        if operator not in BINARY_OPERATORS:
            raise ValueError("Unsupported operator: " + operator)
        
        if operand2 is None:
            raise ValueError("Binary operator requires two operands")
        
        self._validate_pair_bool(operand1, operand2)
        return self._apply_binary(operand1, operand2, operator)

    def _validate_single_bool(self, value):
        if not isinstance(value, bool):
            raise ValueError("Operand must be boolean")

    def _validate_pair_bool(self, a, b):
        if not isinstance(a, bool) or not isinstance(b, bool):
            raise ValueError("Both operands must be boolean")

    def _apply_unary(self, value):
        return not value

    def _apply_binary(self, a, b, op):
        if op == 'and':
            return a & b
        if op == 'or':
            return a | b
        return False

if __name__ == '__main__':
    checker = LogicChecker()
    
    result_and = checker.evaluate(True, False, 'and')
    print(result_and)
    
    result_or = checker.evaluate(True, False, 'or')
    print(result_or)
    
    result_not = checker.evaluate(True, None, 'not')
    print(result_not)
    
    result_false_and = checker.evaluate(False, False, 'and')
    print(result_false_and)