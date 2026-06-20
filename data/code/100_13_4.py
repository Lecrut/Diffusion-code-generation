class LogicChecker:

    def evaluate(self, operand1: bool, operand2: bool, operator: str) -> bool:
        if operator == 'and':
            return operand1 & operand2
        elif operator == 'or':
            return operand1 | operand2
        elif operator == 'not':
            if operand2 is not None:
                raise ValueError('Not operator requires only one operand')
            return not operand1
        else:
            raise ValueError('Invalid operator')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    print(checker.evaluate(False, None, 'not'))