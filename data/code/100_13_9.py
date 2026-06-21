TRUE_VAL = True
FALSE_VAL = False
AND_OP = 'and'
OR_OP = 'or'
NOT_OP = 'not'
UNARY_OPERATORS = (NOT_OP,)
BINARY_OPERATORS = (AND_OP, OR_OP)

class LogicChecker:
    def evaluate(self, operand1, operand2=None, operator=AND_OP):
        is_unary = operator in UNARY_OPERATORS
        if is_unary:
            if operand2 is not None:
                raise ValueError("Unary operator requires no second operand")
            if not isinstance(operand1, bool):
                raise ValueError("Operand must be boolean")
            return not operand1
        
        if operator not in BINARY_OPERATORS:
            raise ValueError("Unsupported operator")
        if not isinstance(operand1, bool) or not isinstance(operand2, bool):
            raise ValueError("Operands must be boolean")
            
        if operator == AND_OP:
            return operand1 & operand2
        if operator == OR_OP:
            return operand1 | operand2
        return FALSE_VAL

if __name__ == '__main__':
    checker = LogicChecker()
    res_and = checker.evaluate(TRUE_VAL, FALSE_VAL, AND_OP)
    res_or = checker.evaluate(TRUE_VAL, FALSE_VAL, OR_OP)
    res_not = checker.evaluate(TRUE_VAL, operator=NOT_OP)
    print(res_and)
    print(res_or)
    print(res_not)