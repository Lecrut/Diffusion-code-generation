class LogicalExpressionEvaluator:
    def __init__(self, value1, value2, value3):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3

    def evaluate_expression(self):
        condition_a = self.value1 < self.value2
        condition_b = self.value3 > self.value2
        result = not (condition_a and condition_b)
        return result

if __name__ == '__main__':
    evaluator = LogicalExpressionEvaluator(5, 10, 15)
    result = evaluator.evaluate_expression()
    print(f"Result of the expression: {result}")