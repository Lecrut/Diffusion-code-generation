class LogicChecker:
    def evaluate(self, operand1, operand2, operator):
        if not isinstance(operand1, bool) or not isinstance(operand2, bool):
            raise ValueError("Operands must be boolean values")
        
        if operator == 'and':
            return operand1 and operand2
        elif operator == 'or':
            return operand1 or operand2
        elif operator == 'not':
            if operand2 is None:
                return not operand1
            else:
                raise ValueError("Operator 'not' requires only one operand")
        else:
            raise ValueError(f"Unsupported operator: {operator}")

if __name__ == '__main__':
    checker = LogicChecker()
    result1 = checker.evaluate(True, False, 'and')
    print(result1)
    result2 = checker.evaluate(True, False, 'or')
    print(result2)
    result3 = checker.evaluate(True, None, 'not')
    print(result3)
    result4 = checker.evaluate(False, True, 'and')
    print(result4)
    result5 = checker.evaluate(False, False, 'or')
    print(result5)