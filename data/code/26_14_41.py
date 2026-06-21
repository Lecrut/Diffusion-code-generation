class IntegerEvaluator:
    def __init__(self, number):
        self.number = number

    def is_greater_than(self, other_number):
        return self.number > other_number

if __name__ == '__main__':
    sample_number1 = 25
    sample_number2 = 20
    evaluator = IntegerEvaluator(sample_number1)
    result1 = evaluator.is_greater_than(sample_number2)
    print(f"Is {sample_number1} greater than {sample_number2}? {result1}")

    sample_number3 = 10
    result2 = evaluator.is_greater_than(sample_number3)
    print(f"Is {sample_number1} greater than {sample_number3}? {result2}")