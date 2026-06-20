class LogicChecker:

    def evaluate(self, a: bool, b: bool, operator: str) -> bool:
        if operator == 'and':
            return a & b
        elif operator == 'or':
            return a | b
        elif operator == 'not':
            if a and (not b):
                return True
            else:
                return False
        else:
            raise ValueError('Invalid operator')
if __name__ == '__main__':
    checker = LogicChecker()
    print(checker.evaluate(True, False, 'and'))
    print(checker.evaluate(True, True, 'or'))
    print(checker.evaluate(False, True, 'not'))