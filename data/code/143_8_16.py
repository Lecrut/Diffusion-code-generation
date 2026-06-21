class LogicalContradictionDetector:
    OPERATORS = {
        "AND": lambda x, y: x and y,
        "OR": lambda x, y: x or y,
        "NOT": lambda x: not x
    }

    @staticmethod
    def evaluate_expression(expression):
        return eval(expression)

    @classmethod
    def check_contradiction(cls, expr1, expr2):
        value1 = cls.evaluate_expression(expr1)
        value2 = cls.evaluate_expression(expr2)
        return cls.OPERATORS.get("NOT", lambda x: False)(value1) == value2 or \
               cls.OPERATORS.get("NOT", lambda x: False)(value2) == value1

if __name__ == '__main__':
    detector = LogicalContradictionDetector()
    print(detector.check_contradiction("True and False", "False"))