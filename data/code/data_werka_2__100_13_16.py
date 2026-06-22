class LogicChecker:
    def evaluate(self, operand1, operand2, operator):
        if not isinstance(operand1, bool) or not isinstance(operand2, bool):
            raise ValueError("Operands must be boolean")
        
        if operator == 'and':
            return operand1 and operand2
        elif operator == 'or':
            return operand1 or operand2
        elif operator == 'not':
            if operand2 is not None:
                raise ValueError("Operator 'not' requires only one operand")
            return not operand1
        else:
            raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    checker = LogicChecker()
    result_and = checker.evaluate(True, False, 'and')
    print(result_and)
    result_or = checker.evaluate(True, False, 'or')
    print(result_or)
    result_not = checker.evaluate(True, None, 'not')
    print(result_not)