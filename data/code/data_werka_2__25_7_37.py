class NumberEvaluator:
    def __init__(self, value):
        self.value = value

    def is_zero(self):
        try:
            number = float(self.value)
            return number == 0
        except ValueError:
            return False

if __name__ == '__main__':
    test_values = ["0", "0.0", "-0", "1", "abc", "0x0", "0b0"]
    evaluators = [NumberEvaluator(value) for value in test_values]
    
    for evaluator in evaluators:
        print(f"'{evaluator.value}' is zero: {evaluator.is_zero()}")