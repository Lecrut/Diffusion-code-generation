class NumberEvaluator:
    def __init__(self, num1, num2):
        self.num1 = self._validate_input(num1)
        self.num2 = self._validate_input(num2)

    def _validate_input(self, value):
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Invalid input: {value} is not an integer.")

    def is_strictly_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    try:
        evaluator = NumberEvaluator(10, 5)
        print(evaluator.is_strictly_greater())
        evaluator = NumberEvaluator(3, 7)
        print(evaluator.is_strictly_greater())
    except ValueError as e:
        print(e)