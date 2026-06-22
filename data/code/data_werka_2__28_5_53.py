class NumberEvaluator:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def evaluate_greater_than(self) -> bool:
        return self.num1 > self.num2

    def evaluate_less_than(self) -> bool:
        return self.num1 < self.num2

    def compare_and_report(self) -> bool:
        return self.evaluate_greater_than()

if __name__ == '__main__':
    evaluator = NumberEvaluator(7.0, 3.2)
    result1 = evaluator.evaluate_greater_than()
    result2 = evaluator.evaluate_less_than()
    result3 = evaluator.compare_and_report()
    
    print("Is num1 strictly greater than num2?", result1)
    print("Is num1 strictly less than num2?", result2)
    print("Compare and report:", result3)