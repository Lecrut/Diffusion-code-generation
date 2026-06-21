class NumberEvaluator:
    INTEGER_TYPE = int

    @staticmethod
    def validate_input(value):
        if not isinstance(value, NumberEvaluator.INTEGER_TYPE):
            raise ValueError(f"Invalid input: {value} is not an integer.")
        return value

    def __init__(self, num1, num2):
        self.num1 = self.validate_input(num1)
        self.num2 = self.validate_input(num2)

    def is_strictly_greater(self):
        return self.num1 > self.num2

if __name__ == '__main__':
    try:
        evaluator1 = NumberEvaluator(15, 10)
        print(evaluator1.is_strictly_greater())
        evaluator2 = NumberEvaluator(8, 12)
        print(evaluator2.is_strictly_greater())
    except ValueError as e:
        print(e)