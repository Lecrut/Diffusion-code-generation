class LogicChecker:

    def evaluate(self, operand1: bool, operand2: bool, operator: str) -> bool:
        if operator == 'and':
            return operand1 & operand2
        elif operator == 'or':
            return operand1 | operand2
        elif operator == 'not':
            if operand1 and operand2:
                raise ValueError("Invalid use of 'not' with two operands")
            return not operand1
        else:
            raise ValueError(f'Unsupported operator: {operator}')
if __name__ == '__main__':
    logic_checker = LogicChecker()
    print(logic_checker.evaluate(True, False, 'and'))
    print(logic_checker.evaluate(True, True, 'or'))
    print(logic_checker.evaluate(False, False, 'not'))